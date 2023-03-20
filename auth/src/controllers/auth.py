from db.users import select_one_by
from helpers.auth import generate_access, generate_refresh, check_password
import jwt
from config.environment import REFRESH_TOKEN_SECRET


def login(data):
    if 'username' not in data:
        return {'message': 'username is required'}, 400
    if 'password' not in data:
        return {'message': 'password is required'}, 400
        
    username = data['username']
    password = data['password']
    if username == "":
        return {'message': 'username can not be empty'}, 400
    if password == "":
        return {'message': 'password can not be empty'}, 400
    
    user = select_one_by('username', username)
    if user:
        hashed_password = user[2]
        if check_password(password, hashed_password):
            access_token = generate_access(user[0], username)
            refresh_token = generate_refresh(user[0], username)
            return {"access_token":access_token, "refresh_token":refresh_token}
    
    return 'Invalid credential try again'


def token(headers):
    token = headers.get('Authorization', '')
    if token == '':
        return {'message': 'Token is required'}, 400
    token = token.split(' ')[1]
    unverified_headers = jwt.get_unverified_header(token)
    payload = jwt.decode(token, key = REFRESH_TOKEN_SECRET, algorithms = unverified_headers.get('alg'))
    id = payload.get('sub')
    username = payload.get('username')
    return {"access_token": generate_access(id, username)}