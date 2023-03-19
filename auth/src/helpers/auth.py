from datetime import datetime, timedelta
import jwt
import bcrypt
from config.environment import ACCESS_TOKEN_SECRET, REFRESH_TOKEN_SECRET
def generate_access(id):
    now = datetime.now()
    payload = {
        "sub": id,
        "iat": now.timestamp(),
        "exp": (now + timedelta(seconds=30)).timestamp(),
    }
    access_token = jwt.encode(payload = payload, key= 'ACCESS_TOKEN_SECRET', algorithm='HS256')
    return access_token

def generate_refresh(id):
    now = datetime.now()
    payload = {
        "sub": id,
        "iat": now.timestamp(),
        "exp": (now + timedelta(days=1)).timestamp(),
    }
    refresh_token = jwt.encode(payload = payload, key = 'REFRESH_TOKEN_SECRET',  algorithm='HS256')
    return refresh_token

def check_password(password, hashed_password):
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))
