from db.users import select_one_by
from helpers.auth import generate_access, generate_refresh, check_password


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
        print(user)
        hashed_password = user[2]
        if check_password(password, hashed_password):
            access_token = generate_access(user[0])
            refresh_token = generate_refresh(user[0])
            return {"access_token":access_token, "refresh_token":refresh_token}
    
    return 'Invalid credential try again'