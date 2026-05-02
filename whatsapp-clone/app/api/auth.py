import secrets
import random
from flask import Blueprint, request, jsonify
from ..models import User
from ..database import db
from ..otp_service import send_otp
from ..redis_client import (
    verify_otp, set_session, delete_session, set_user_online, get_session
)

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/send-otp', methods=['POST'])
def api_send_otp():
    data = request.json
    phone = data.get('phone_number', '').strip()
    if not phone:
        return jsonify({'success': False, 'message': 'Phone number required'}), 400
    result = send_otp(phone)
    return jsonify(result)


@auth_bp.route('/verify-otp', methods=['POST'])
def api_verify_otp():
    data = request.json
    phone = data.get('phone_number', '').strip()
    code = data.get('code', '').strip()

    if not verify_otp(phone, code):
        return jsonify({'success': False, 'message': 'Invalid or expired OTP'}), 400

    user = User.query.filter_by(phone_number=phone).first()
    is_new = False
    if not user:
        colors = [
            '#25D366', '#128C7E', '#075E54', '#34B7F1',
            '#ECE5DD', '#FF6B6B', '#4ECDC4',
        ]
        user = User(
            phone_number=phone,
            name=phone,
            avatar_color=random.choice(colors),
        )
        db.session.add(user)
        db.session.commit()
        is_new = True

    token = secrets.token_urlsafe(32)
    set_session(token, user.id)
    set_user_online(user.id, True)

    return jsonify({
        'success': True,
        'token': token,
        'user': user.to_dict(),
        'is_new': is_new,
    })


@auth_bp.route('/logout', methods=['POST'])
def api_logout():
    token = request.headers.get('X-Session-Token')
    if token:
        user_id = get_session(token)
        if user_id:
            set_user_online(user_id, False)
        delete_session(token)
    return jsonify({'success': True})


@auth_bp.route('/me', methods=['GET'])
def api_me():
    token = request.headers.get('X-Session-Token')
    if not token:
        return jsonify({'success': False}), 401
    user_id = get_session(token)
    if not user_id:
        return jsonify({'success': False}), 401
    user = User.query.get(user_id)
    if not user:
        return jsonify({'success': False}), 401
    set_user_online(user_id, True)  # heartbeat
    return jsonify({'success': True, 'user': user.to_dict()})


@auth_bp.route('/update-profile', methods=['POST'])
def api_update_profile():
    token = request.headers.get('X-Session-Token')
    user_id = get_session(token)
    if not user_id:
        return jsonify({'success': False}), 401
    data = request.json
    user = User.query.get(user_id)
    if not user:
        return jsonify({'success': False}), 404
    if data.get('name'):
        user.name = data['name']
    if data.get('about'):
        user.about = data['about']
    db.session.commit()
    return jsonify({'success': True, 'user': user.to_dict()})


@auth_bp.route('/users/search', methods=['GET'])
def api_search_users():
    token = request.headers.get('X-Session-Token')
    user_id = get_session(token)
    if not user_id:
        return jsonify({'success': False}), 401
    q = request.args.get('q', '').strip()
    if len(q) < 2:
        return jsonify({'users': []})
    users = User.query.filter(
        (User.phone_number.ilike(f'%{q}%') | User.name.ilike(f'%{q}%')),
        User.id != user_id,
    ).limit(20).all()
    return jsonify({'users': [u.to_dict() for u in users]})
