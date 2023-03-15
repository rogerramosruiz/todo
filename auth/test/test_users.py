import requests
import string
import random

ENDPOINT = 'http://localhost:3000/api/v1'

def sign_up(json_paload):
    return requests.post(f'{ENDPOINT}/signup', json=json_paload)

def random_string(length:int = 10):
    chars = string.ascii_letters + string.digits
    rand_str = ''
    for i in range(length):
        rand_str += random.choice(chars)
    return rand_str


def gen_user():
    password = random_string()
    return  {
        'username': random_string(),
        'password': password,
        'confirmation_password': password
    }

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
    payload_user = {
        'password': 'test password',
        'confirmation_password': 'test password'
    }
    r = sign_up(payload_user)
    assert r.status_code == 400
    assert r.json()['message'] == 'username is required'
    
    # no password 
    payload_user = {
        'username': 'user test 1',
        'confirmation_password': 'abcde'
    }
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