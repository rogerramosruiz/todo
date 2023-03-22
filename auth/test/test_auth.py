from helpers import random_string, gen_user
from request import sign_up, login, refresh_token, logout

import time

def test_login():
    user = gen_user()
    sign_up(user)
    user.pop('confirmation_password')

    r = login(user)
    assert r.status_code == 200
    json_resp = r.json()
    assert 'access_token' in json_resp
    assert 'refresh_token' in json_resp

def test_login_validations():
    # no username in payload
    user = {
        'username' :'user test',
        'password' : '123456'
    }
    user.pop('username')
    r = login(user)
    assert r.status_code == 400
    assert r.json()['message'] == 'username is required'

    # no password in payload
    user = {
        'username' :'user test',
        'password' : '123456'
    }
    user.pop('password')
    r = login(user)
    assert r.status_code == 400
    print(r.json())
    assert r.json()['message'] == 'password is required'
    
    # username empty
    user = {
        'username' :'',
        'password' : '123456'
    }
    r = login(user)
    assert r.status_code == 400
    assert r.json()['message'] == 'username can not be empty'
    # password empty
    user = {
        'username' :'test user',
        'password' : ''
    }
    r = login(user)
    assert r.status_code == 400
    assert r.json()['message'] == 'password can not be empty'

    # invalid credentials
    user = gen_user()
    user.pop('confirmation_password')

    r = login(user)
    assert r.status_code == 400
    assert r.json()['message'] == 'invalid credentials try again'

def test_refresh_token():
    user = gen_user()
    sign_up(user)
    user.pop('confirmation_password')
    r = login(user)

    json_resp = r.json()
    access_token = json_resp['access_token']
    refresh_token_r = json_resp['refresh_token']
    # wait in order to not cause an error of iat
    time.sleep(1)
    r = refresh_token(refresh_token_r)
    json_resp = r.json()
    assert 'access_token' in json_resp
    new_access_token = json_resp['access_token']
    assert r.status_code == 200
    assert new_access_token != access_token


def test_refresh_token_validations():
    r = refresh_token(None)
    assert r.status_code == 401
    assert r.json()['message'] == 'invalid token'

    invalid_token = f'{random_string(36)}.{random_string(107)}.{random_string(43)}'
    r = refresh_token(invalid_token)
    assert r.status_code == 401
    assert r.json()['message'] == 'invalid token'

    invalid_token = f'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.{random_string(107)}.{random_string(43)}'
    r = refresh_token(invalid_token)
    assert r.status_code == 401
    assert r.json()['message'] == 'Signature verification failed'

def test_logout():
    user = gen_user()
    sign_up(user)
    user.pop('confirmation_password')
    
    r = login(user)
    json_resp = r.json()
    refresh_token_r = json_resp['refresh_token']
    
    # wait in order to not cause an error of iat
    time.sleep(1)
    
    r = logout(refresh_token_r)
    assert r.status_code == 200
    assert r.json()['message'] == 'success'

    r = refresh_token(refresh_token_r)
    assert r.status_code == 401
    assert r.json()['message'] == 'invalid token'

