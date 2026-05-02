from datetime import datetime
from .database import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    phone_number = db.Column(db.String(20), unique=True, nullable=False)
    name = db.Column(db.String(100))
    about = db.Column(db.String(500), default='Hey there! I am using WhatsApp Clone.')
    avatar_color = db.Column(db.String(7), default='#25D366')
    is_online = db.Column(db.Boolean, default=False)
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'phone_number': self.phone_number,
            'name': self.name or self.phone_number,
            'about': self.about,
            'avatar_color': self.avatar_color,
            'is_online': self.is_online,
            'last_seen': self.last_seen.isoformat() if self.last_seen else None,
        }


class Conversation(db.Model):
    __tablename__ = 'conversations'
    id = db.Column(db.Integer, primary_key=True)
    is_group = db.Column(db.Boolean, default=False)
    group_name = db.Column(db.String(100))
    group_avatar_color = db.Column(db.String(7), default='#25D366')
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    members = db.relationship('ConversationMember', backref='conversation', lazy='dynamic')
    messages = db.relationship(
        'Message', backref='conversation', lazy='dynamic',
        order_by='Message.created_at'
    )


class ConversationMember(db.Model):
    __tablename__ = 'conversation_members'
    id = db.Column(db.Integer, primary_key=True)
    conversation_id = db.Column(
        db.Integer, db.ForeignKey('conversations.id', ondelete='CASCADE')
    )
    user_id = db.Column(
        db.Integer, db.ForeignKey('users.id', ondelete='CASCADE')
    )
    joined_at = db.Column(db.DateTime, default=datetime.utcnow)
    __table_args__ = (db.UniqueConstraint('conversation_id', 'user_id'),)


class Message(db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True)
    conversation_id = db.Column(
        db.Integer, db.ForeignKey('conversations.id', ondelete='CASCADE')
    )
    sender_id = db.Column(
        db.Integer, db.ForeignKey('users.id', ondelete='CASCADE')
    )
    content = db.Column(db.Text, nullable=False)
    message_type = db.Column(db.String(20), default='text')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_deleted = db.Column(db.Boolean, default=False)
    sender = db.relationship('User', backref='messages')

    def to_dict(self):
        return {
            'id': self.id,
            'conversation_id': self.conversation_id,
            'sender_id': self.sender_id,
            'sender_name': (
                self.sender.name or self.sender.phone_number
                if self.sender else 'Unknown'
            ),
            'sender_color': self.sender.avatar_color if self.sender else '#25D366',
            'content': self.content,
            'type': self.message_type,
            'created_at': self.created_at.isoformat(),
            'is_deleted': self.is_deleted,
        }


class MessageReceipt(db.Model):
    __tablename__ = 'message_receipts'
    id = db.Column(db.Integer, primary_key=True)
    message_id = db.Column(
        db.Integer, db.ForeignKey('messages.id', ondelete='CASCADE')
    )
    user_id = db.Column(
        db.Integer, db.ForeignKey('users.id', ondelete='CASCADE')
    )
    status = db.Column(db.String(20), default='sent')
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    __table_args__ = (db.UniqueConstraint('message_id', 'user_id'),)
