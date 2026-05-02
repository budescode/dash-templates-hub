import eventlet
eventlet.monkey_patch()

from app.server import create_app, socketio

app, server, socketio_instance = create_app()

if __name__ == '__main__':
    socketio_instance.run(server, host='0.0.0.0', port=8050, debug=True, use_reloader=False)
