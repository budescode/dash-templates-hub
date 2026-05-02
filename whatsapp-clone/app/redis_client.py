import redis
from .config import Config

_redis = None


def get_redis():
    global _redis
    if _redis is None:
        _redis = redis.from_url(Config.REDIS_URL, decode_responses=True)
    return _redis


def set_user_online(user_id, online=True):
    r = get_redis()
    key = f"user:online:{user_id}"
    if online:
        r.setex(key, 60, "1")  # expire after 60 seconds (heartbeat needed)
    else:
        r.delete(key)


def is_user_online(user_id):
    r = get_redis()
    return bool(r.get(f"user:online:{user_id}"))


def set_typing(conversation_id, user_id, is_typing):
    r = get_redis()
    key = f"typing:{conversation_id}:{user_id}"
    if is_typing:
        r.setex(key, 5, "1")
    else:
        r.delete(key)


def get_typing_users(conversation_id, exclude_user_id):
    r = get_redis()
    pattern = f"typing:{conversation_id}:*"
    keys = r.keys(pattern)
    typing = []
    for key in keys:
        uid = int(key.split(":")[-1])
        if uid != exclude_user_id:
            typing.append(uid)
    return typing


def store_otp(phone_number, code, ttl=300):
    r = get_redis()
    r.setex(f"otp:{phone_number}", ttl, code)


def verify_otp(phone_number, code):
    r = get_redis()
    stored = r.get(f"otp:{phone_number}")
    if stored and stored == code:
        r.delete(f"otp:{phone_number}")
        return True
    return False


def set_session(session_token, user_id, ttl=86400 * 7):
    r = get_redis()
    r.setex(f"session:{session_token}", ttl, str(user_id))


def get_session(session_token):
    r = get_redis()
    val = r.get(f"session:{session_token}")
    return int(val) if val else None


def delete_session(session_token):
    r = get_redis()
    r.delete(f"session:{session_token}")
