import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-change-me')
    DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://postgres:postgres123@localhost:5432/whatsapp_clone')
    REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379/0')
    OTP_DEV_MODE = os.getenv('OTP_DEV_MODE', 'true').lower() == 'true'
    OTP_TTL = 300  # 5 minutes
    SESSION_COOKIE_SECURE = False
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    UPLOAD_FOLDER = 'uploads'
    DEBUG = os.getenv('DEBUG', 'true').lower() == 'true'

    # Twilio (optional)
    TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
    TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
    TWILIO_PHONE = os.getenv('TWILIO_PHONE')
