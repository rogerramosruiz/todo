from db.users import select_one_by
from helpers.auth import check_password, generate_token
from flask import g

from redis_client.ops import add
from helpers.time_math import dif_time

def login(data):
    if 'username' not in data:
        return {'message': 'username is required'}, 400
    if 'password' not in data:
        return {'message': 'password is required'}, 400
        
    username = data['username']
    password = data['password']
    if username == '':
        return {'message': 'username can not be empty'}, 400
    if password == '':
        return {'message': 'password can not be empty'}, 400
    
    user = select_one_by('username', username)
    if user:
        hashed_password = user[2]
        if check_password(password, hashed_password):
            access_token, access_expiration = generate_token(user[0], username, access=True)
            refresh_token, refresh_expiration = generate_token(user[0], username, access=False)
            return {'access_token': access_token, 
                    'expires_in': access_expiration,
                    'refresh_token': refresh_token,
                    'refresh_token_expires_in': refresh_expiration
                    }
    
    return {'message': 'invalid credentials try again'}, 400 

def logout():
    token = g.token
    redis_exp = dif_time(g.payload['exp'])
    add(token, '0', redis_exp)
    return {'message': 'success'}

def token():
    payload = g.payload
    id = payload['sub']
    username = payload['username']
    access_token, expiration = generate_token(id, username, access=True)
    return {'access_token': access_token, 'expires_in': expiration}