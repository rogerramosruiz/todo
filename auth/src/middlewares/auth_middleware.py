from functools import wraps
from flask import request, g
from helpers.auth import verify_token

def refresh_token_verifier(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        headers = request.headers
        token = headers.get('Authorization', '')
        if token == '':
            return {'message': 'Token is required'}, 400
        token = token.split(' ')[1].strip()
        try:
            g.payload = verify_token(token, access=False)
            g.token = token
        except Exception as e:
            return {'message': str(e)}, 401
    
        return func(*args, **kwargs)
    return decorated