def register_callbacks(app):
    from .auth import register_auth_callbacks
    from .chat import register_chat_callbacks
    register_auth_callbacks(app)
    register_chat_callbacks(app)
