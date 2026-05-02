"""
Socket.IO event handlers.
Real-time typing and presence are handled via Redis + polling in the MVP.
This module registers optional Socket.IO events for enhanced real-time features.
"""
from .server import socketio
from .redis_client import get_session, set_user_online


@socketio.on('connect')
def handle_connect():
    pass


@socketio.on('disconnect')
def handle_disconnect():
    pass


@socketio.on('join_conversation')
def handle_join(data):
    from flask_socketio import join_room
    conv_id = data.get('conversation_id')
    if conv_id:
        join_room(f'conv_{conv_id}')


@socketio.on('leave_conversation')
def handle_leave(data):
    from flask_socketio import leave_room
    conv_id = data.get('conversation_id')
    if conv_id:
        leave_room(f'conv_{conv_id}')
