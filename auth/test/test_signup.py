from helpers import random_string, sign_up, gen_user


def test_sign_up():
    payload_user = gen_user()
    # signup tests
    r = sign_up(payload_user)
    assert r.status_code == 201
    assert r.json()['message'] == 'Success'
    
    # test no duplicate username
    r = sign_up(payload_user)
    assert r.status_code == 409
    assert r.json()['message'] == 'username is already taken. chose another'
    
    # test password match
    payload_user = gen_user()
    payload_user['password'] = random_string()
    r = sign_up(payload_user)
    assert r.status_code == 400
    assert r.json()['message'] == "passwords don't match"

def test_signup_data_validation():
    # no username
    payload_user = gen_user()
    payload_user.pop('username')
    r = sign_up(payload_user)
    assert r.status_code == 400
    assert r.json()['message'] == 'username is required'
    
    # no password 
    payload_user = gen_user()
    payload_user.pop('password')
    r = sign_up(payload_user)
    assert r.status_code == 400
    assert r.json()['message'] == 'password is required'
    
    # no confirmation password 
    payload_user = {
        'username': 'user test 1',
        'password': 'test password',
    }
    r = sign_up(payload_user)
    assert r.status_code == 400
    assert r.json()['message'] == 'confirmation_password is required'

    # empty username
    payload_user = gen_user()
    payload_user['username'] = ''
    r = sign_up(payload_user)
    assert r.status_code == 400
    assert r.json()['message'] == 'username can not be empty'
    
    # empty password
    payload_user = gen_user()
    payload_user['password'] = ''
    payload_user['confirmation_password'] = ''
    r = sign_up(payload_user)
    assert r.status_code == 400
    assert r.json()['message'] == 'password can not be empty'