"""
WSGI entry point for production deployment with Gunicorn
Usage: gunicorn --workers 4 wsgi:app.server
"""

from app.application import app

if __name__ == '__main__':
    app.run_server(debug=False)
