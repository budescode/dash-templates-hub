from datetime import datetime
from flask import Blueprint, request, jsonify
from ..models import (
    Conversation, ConversationMember, Message, User, MessageReceipt
)
from ..database import db
from ..redis_client import (
    get_session, set_typing, get_typing_users, is_user_online
)

messages_bp = Blueprint('messages', __name__)


def get_current_user(req):
    token = req.headers.get('X-Session-Token')
    if not token:
        return None
    user_id = get_session(token)
    if not user_id:
        return None
    return User.query.get(user_id)


@messages_bp.route('/conversations', methods=['GET'])
def get_conversations():
    user = get_current_user(request)
    if not user:
        return jsonify({'success': False}), 401

    memberships = ConversationMember.query.filter_by(user_id=user.id).all()
    result = []
    for m in memberships:
        conv = m.conversation
        last_msg = (
            Message.query
            .filter_by(conversation_id=conv.id, is_deleted=False)
            .order_by(Message.created_at.desc())
            .first()
        )

        # For 1-1 chats, get the other user
        other_user = None
        if not conv.is_group:
            other_member = ConversationMember.query.filter(
                ConversationMember.conversation_id == conv.id,
                ConversationMember.user_id != user.id,
            ).first()
            if other_member:
                other_user = User.query.get(other_member.user_id)

        unread_count = 0
        if last_msg and last_msg.sender_id != user.id:
            # Count unread: messages from others that we haven't marked read
            subq = (
                db.session.query(MessageReceipt.message_id)
                .filter(
                    MessageReceipt.user_id == user.id,
                    MessageReceipt.status == 'read',
                )
                .subquery()
            )
            unread_count = (
                Message.query
                .filter(
                    Message.conversation_id == conv.id,
                    Message.sender_id != user.id,
                    Message.is_deleted == False,
                    ~Message.id.in_(subq),
                )
                .count()
            )

        result.append({
            'id': conv.id,
            'is_group': conv.is_group,
            'name': (
                conv.group_name if conv.is_group
                else (
                    other_user.name or other_user.phone_number
                    if other_user else 'Unknown'
                )
            ),
            'avatar_color': (
                conv.group_avatar_color if conv.is_group
                else (other_user.avatar_color if other_user else '#25D366')
            ),
            'other_user': other_user.to_dict() if other_user else None,
            'last_message': (
                last_msg.content
                if last_msg and not last_msg.is_deleted
                else ('This message was deleted' if last_msg else '')
            ),
            'last_message_time': (
                last_msg.created_at.isoformat()
                if last_msg else conv.created_at.isoformat()
            ),
            'last_message_sender_id': last_msg.sender_id if last_msg else None,
            'unread_count': unread_count,
            'is_online': is_user_online(other_user.id) if other_user else False,
        })

    result.sort(key=lambda x: x['last_message_time'], reverse=True)
    return jsonify({'conversations': result})


@messages_bp.route('/conversations', methods=['POST'])
def create_conversation():
    user = get_current_user(request)
    if not user:
        return jsonify({'success': False}), 401

    data = request.json
    other_user_id = data.get('user_id')

    if other_user_id:
        # Check if 1-1 conversation already exists
        existing = (
            db.session.query(Conversation)
            .join(ConversationMember, Conversation.id == ConversationMember.conversation_id)
            .filter(
                ConversationMember.user_id == user.id,
                Conversation.is_group == False,
            )
            .all()
        )

        for conv in existing:
            members = [
                m.user_id
                for m in ConversationMember.query.filter_by(
                    conversation_id=conv.id
                ).all()
            ]
            if (
                other_user_id in members
                and user.id in members
                and len(members) == 2
            ):
                return jsonify({
                    'success': True,
                    'conversation_id': conv.id,
                    'existing': True,
                })

        conv = Conversation(is_group=False, created_by=user.id)
        db.session.add(conv)
        db.session.flush()
        db.session.add(ConversationMember(conversation_id=conv.id, user_id=user.id))
        db.session.add(
            ConversationMember(conversation_id=conv.id, user_id=other_user_id)
        )
        db.session.commit()
        return jsonify({
            'success': True,
            'conversation_id': conv.id,
            'existing': False,
        })

    # Group chat
    member_ids = data.get('member_ids', [])
    group_name = data.get('group_name', 'New Group')
    conv = Conversation(is_group=True, group_name=group_name, created_by=user.id)
    db.session.add(conv)
    db.session.flush()
    all_members = list(set([user.id] + member_ids))
    for uid in all_members:
        db.session.add(ConversationMember(conversation_id=conv.id, user_id=uid))
    db.session.commit()
    return jsonify({'success': True, 'conversation_id': conv.id})


@messages_bp.route('/conversations/<int:conv_id>/messages', methods=['GET'])
def get_messages(conv_id):
    user = get_current_user(request)
    if not user:
        return jsonify({'success': False}), 401

    member = ConversationMember.query.filter_by(
        conversation_id=conv_id, user_id=user.id
    ).first()
    if not member:
        return jsonify({'success': False, 'message': 'Not a member'}), 403

    since_id = request.args.get('since_id', 0, type=int)
    limit = request.args.get('limit', 50, type=int)

    if since_id:
        messages = (
            Message.query
            .filter_by(conversation_id=conv_id)
            .filter(Message.id > since_id)
            .order_by(Message.created_at.asc())
            .all()
        )
        for msg in messages:
            if msg.sender_id != user.id:
                receipt = MessageReceipt.query.filter_by(
                    message_id=msg.id, user_id=user.id
                ).first()
                if not receipt:
                    db.session.add(
                        MessageReceipt(
                            message_id=msg.id, user_id=user.id, status='read'
                        )
                    )
        db.session.commit()
        return jsonify({'messages': [m.to_dict() for m in messages]})

    # Initial load - get last N messages
    messages = (
        Message.query
        .filter_by(conversation_id=conv_id)
        .order_by(Message.created_at.desc())
        .limit(limit)
        .all()
    )
    messages = messages[::-1]

    for msg in messages:
        if msg.sender_id != user.id:
            receipt = MessageReceipt.query.filter_by(
                message_id=msg.id, user_id=user.id
            ).first()
            if not receipt:
                db.session.add(
                    MessageReceipt(
                        message_id=msg.id, user_id=user.id, status='read'
                    )
                )
            elif receipt.status != 'read':
                receipt.status = 'read'
                receipt.updated_at = datetime.utcnow()
    db.session.commit()
    return jsonify({'messages': [m.to_dict() for m in messages]})


@messages_bp.route('/conversations/<int:conv_id>/messages', methods=['POST'])
def send_message(conv_id):
    user = get_current_user(request)
    if not user:
        return jsonify({'success': False}), 401

    member = ConversationMember.query.filter_by(
        conversation_id=conv_id, user_id=user.id
    ).first()
    if not member:
        return jsonify({'success': False}), 403

    data = request.json
    content = data.get('content', '').strip()
    if not content:
        return jsonify({'success': False, 'message': 'Empty message'}), 400

    msg = Message(
        conversation_id=conv_id,
        sender_id=user.id,
        content=content,
        message_type=data.get('type', 'text'),
    )
    db.session.add(msg)
    db.session.flush()

    # Create receipt for sender (sent)
    db.session.add(MessageReceipt(message_id=msg.id, user_id=user.id, status='sent'))
    db.session.commit()

    return jsonify({'success': True, 'message': msg.to_dict()})


@messages_bp.route('/conversations/<int:conv_id>/typing', methods=['POST'])
def update_typing(conv_id):
    user = get_current_user(request)
    if not user:
        return jsonify({'success': False}), 401
    data = request.json
    set_typing(conv_id, user.id, data.get('is_typing', False))
    return jsonify({'success': True})


@messages_bp.route('/conversations/<int:conv_id>/typing', methods=['GET'])
def get_typing(conv_id):
    user = get_current_user(request)
    if not user:
        return jsonify({'success': False}), 401
    typing_user_ids = get_typing_users(conv_id, user.id)
    typing_users = []
    for uid in typing_user_ids:
        u = User.query.get(uid)
        if u:
            typing_users.append(u.name or u.phone_number)
    return jsonify({'typing_users': typing_users})
