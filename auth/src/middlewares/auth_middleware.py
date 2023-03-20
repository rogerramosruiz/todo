from functools import wraps
from flask import request, g
import jwt
from jwt.exceptions import ExpiredSignatureError, ImmatureSignatureError, InvalidAlgorithmError, InvalidKeyError, InvalidSignatureError

from config.environment import REFRESH_TOKEN_SECRET

def token_verifier(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        headers = request.headers
        token = headers.get('Authorization', '')
        if token == '':
            return {'message': 'Token is required'}, 400
        token = token.split(' ')[1].strip()
        try:
            unverified_headers = jwt.get_unverified_header(token)
            payload = jwt.decode(token, key = REFRESH_TOKEN_SECRET, algorithms = unverified_headers.get('alg'))
            id = payload.get('sub')
            username = payload.get('username')
            g.id = id
            g.username = username
        except (ExpiredSignatureError, ImmatureSignatureError, InvalidAlgorithmError, InvalidKeyError, InvalidSignatureError) as error:
            return {'message': str(error)},401
        except Exception as e:
            print(e)
            return {'message': 'invalid token'},401
    
        return func(*args, **kwargs)
    return decorated