"""
Adminator Admin Dashboard - Dash Version
Main entry point for running the application
"""

from app.application import app

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8051)
