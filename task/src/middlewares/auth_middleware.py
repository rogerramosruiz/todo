from functools import wraps
from flask import request, g
import requests
from config.environment import AUTH_SERVER

def token_verifier(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        headers = request.headers
        token = headers.get('Authorization', '')
        r = requests.get(f'http://{AUTH_SERVER}/api/v1/auth/verify',headers={
            'Authorization': token
        })
        resp_json = r.json()
        if r.status_code >= 400 and r.status_code <= 401:
            return resp_json, r.status_code
        
        g.id_user = resp_json['data']['sub']
        g.username = resp_json['data']['username']
        return func(*args, **kwargs)
    
    return decorated