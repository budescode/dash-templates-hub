import os
from flask import Flask
from flask_socketio import SocketIO
from dash import Dash, html
import dash_bootstrap_components as dbc
from .config import Config
from .database import db, init_db

socketio = SocketIO()


def create_app():
    server = Flask(__name__)
    server.config['SECRET_KEY'] = Config.SECRET_KEY
    server.config['SQLALCHEMY_DATABASE_URI'] = Config.DATABASE_URL
    server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Init DB
    init_db(server)

    # Init SocketIO with eventlet
    socketio.init_app(
        server,
        cors_allowed_origins="*",
        async_mode='eventlet',
        logger=False,
        engineio_logger=False,
    )

    # Register API blueprints
    from .api.auth import auth_bp
    from .api.messages import messages_bp
    server.register_blueprint(auth_bp, url_prefix='/api/auth')
    server.register_blueprint(messages_bp, url_prefix='/api/messages')

    # Create Dash app
    app = Dash(
        __name__,
        server=server,
        url_base_pathname='/',
        external_stylesheets=[
            dbc.themes.BOOTSTRAP,
            'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css',
        ],
        external_scripts=[
            'https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.5.4/socket.io.min.js',
        ],
        suppress_callback_exceptions=True,
        meta_tags=[
            {'name': 'viewport', 'content': 'width=device-width, initial-scale=1'}
        ],
    )
    app.title = 'WhatsApp Clone'

    # Set layout
    from .layouts.main import get_main_layout
    app.layout = get_main_layout()

    # Register callbacks
    from .callbacks import register_callbacks
    register_callbacks(app)

    return app, server, socketio
