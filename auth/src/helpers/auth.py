from datetime import datetime, timedelta
import jwt
import bcrypt
from config.environment import ACCESS_TOKEN_SECRET, REFRESH_TOKEN_SECRET
def generate_access(id, username):
    now = datetime.now()
    payload = {
        "sub": id,
        "iat": now.timestamp(),
        "exp": (now + timedelta(days=1)).timestamp(),
        "username": username
    }
    access_token = jwt.encode(payload = payload, key= ACCESS_TOKEN_SECRET, algorithm='HS256')
    return access_token

def generate_refresh(id, username):
    now = datetime.now()
    payload = {
        "sub": id,
        "iat": now.timestamp(),
        "exp": (now + timedelta(days=1)).timestamp(),
        "username": username
    }
    # add username 
    refresh_token = jwt.encode(payload = payload, key = REFRESH_TOKEN_SECRET,  algorithm='HS256')
    return refresh_token

def check_password(password, hashed_password):
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))