from db.users import insert, select_one_by
import bcrypt

def signup(data):
    try:
        if 'username' not in data:
            return {'message': 'username is required'}, 400
        if 'password' not in data:
            return {'message': 'password is required'}, 400
        if 'confirmation_password' not in data:
            return {'message': 'confirmation_password is required'}, 400
        
        username = data['username']
        password = data['password']
        confirmation_password = data['confirmation_password']
        
        if username == "":
            return {'message': 'username can not be empty'}, 400
        if password == "":
            return {'message': 'password can not be empty'}, 400
        if confirmation_password == "":
            return {'message': 'confirmation_password can not be empty'}, 400
        
        if password != confirmation_password:
            return {'message': "passwords don't match"}, 400
        
        # check if user exists    
        user = select_one_by('username', username)
        if user is not None:
            return {'message': 'username is already taken. chose another'}, 409
       # create user        
        byte_password = password.encode('utf-8')
        hashed_password = bcrypt.hashpw(byte_password, bcrypt.gensalt())
        insert(username, hashed_password)
        return {'message': 'Success'}, 201
    
    except Exception as e:
        return {'message': 'Internal server error'}, 500
