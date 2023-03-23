from datetime import datetime, timedelta
import jwt
import bcrypt

from jwt.exceptions import ExpiredSignatureError, ImmatureSignatureError, InvalidAlgorithmError, InvalidKeyError, InvalidSignatureError
from redis_client.ops import exists


from config.environment import ACCESS_TOKEN_SECRET, REFRESH_TOKEN_SECRET, ACCESS_TIME, REFRESH_TIME

def select_type(access:bool = True):
    """
    access: bool, True for access_token, False for refresh_token
    """
    if access:
        return ACCESS_TOKEN_SECRET, timedelta(
            days = ACCESS_TIME['days'], hours = ACCESS_TIME['hours'], 
            minutes=ACCESS_TIME['minutes'], seconds=ACCESS_TIME['seconds'])
    
    return REFRESH_TOKEN_SECRET, timedelta(
            days = REFRESH_TIME['days'], hours=REFRESH_TIME['hours'], 
            minutes=REFRESH_TIME['minutes'], seconds=REFRESH_TIME['seconds'])
    

def generate_token(id, username, access:bool = True):
    secret, time_delta = select_type(access)
    now = datetime.now()
    iat = int(now.timestamp())
    expiration = int((now + time_delta).timestamp())
    payload = {
        "sub": id,
        "iat": iat,
        "exp": expiration,
        "username": username
    }
    return jwt.encode(payload = payload, key = secret, algorithm = 'HS256'), expiration
    
def check_password(password, hashed_password):
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

def verify_token(token, access:bool = True):
    secret, _ = select_type(access)
    if exists(token):
        raise Exception('invalid token')
    try:
        unverified_headers = jwt.get_unverified_header(token)
        return jwt.decode(token, key = secret, algorithms = unverified_headers.get('alg'))
    except (ExpiredSignatureError, ImmatureSignatureError, InvalidAlgorithmError, InvalidKeyError, InvalidSignatureError) as error:
        raise error
    except Exception as e:
        print(e)
        raise Exception('invalid token')