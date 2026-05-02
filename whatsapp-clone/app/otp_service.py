import random
import string
from .redis_client import store_otp
from .config import Config


def generate_otp():
    return ''.join(random.choices(string.digits, k=6))


def send_otp(phone_number):
    code = generate_otp()
    store_otp(phone_number, code, Config.OTP_TTL)

    if Config.OTP_DEV_MODE:
        print(f"\n[DEV MODE] OTP for {phone_number}: {code}\n")
        return {
            'success': True,
            'dev_code': code,
            'message': f'OTP sent (dev mode: {code})',
        }

    # Production: Twilio
    if Config.TWILIO_ACCOUNT_SID:
        try:
            from twilio.rest import Client
            client = Client(Config.TWILIO_ACCOUNT_SID, Config.TWILIO_AUTH_TOKEN)
            client.messages.create(
                body=f'Your WhatsApp Clone OTP: {code}',
                from_=Config.TWILIO_PHONE,
                to=phone_number,
            )
            return {'success': True, 'message': 'OTP sent via SMS'}
        except Exception as e:
            return {'success': False, 'message': str(e)}

    return {'success': False, 'message': 'No SMS provider configured'}
