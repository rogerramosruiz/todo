import requests

ENDPOINT = 'http://localhost:3000/api/v1'

def sign_up(json_paload):
    return requests.post(f'{ENDPOINT}/signup', json=json_paload)

def test_sign_up():
    payload_user = {
        "username": "user test",
        "password": "test password",
        "confirmation_password": "test password"
    }
    # signup tests
    r = sign_up(payload_user)
    assert r.status_code == 201
    assert r.json()['message'] == 'Success'
    # test no duplicate username
    r = sign_up(payload_user)
    assert r.status_code == 400
    assert r.json()['message'] == 'this username is already taken. chose another'
    # test password match
    payload_user = {
        "username": "user test 1",
        "password": "test password",
        "confirmation_password": "abcde"
    }
    r = sign_up(payload_user)
    assert r.status_code == 400
    assert r.json()['message'] == "passwords don't match"

def test_signup_data_validation():
    # no username
    payload_user = {
        "password": "test password",
        "confirmation_password": "test password"
    }
    r = sign_up(payload_user)
    assert r.status_code == 400
    assert r.json()['message'] == "username is required"
    # no password 
    payload_user = {
        "username": "user test 1",
        "confirmation_password": "abcde"
    }
    r = sign_up(payload_user)
    assert r.status_code == 400
    assert r.json()['message'] == "password is required"
    # no confirmation password 
    payload_user = {
        "username": "user test 1",
        "password": "test password",
    }
    r = sign_up(payload_user)
    assert r.status_code == 400
    assert r.json()['message'] == "confirmation_password is required"

    # empty username
    payload_user = {
        "username": "",
        "password": "test password",
        "confirmation_password": "test password"
    }
    r = sign_up(payload_user)
    assert r.status_code == 400
    assert r.json()['message'] == "username is can not be empty"
    # empty password
    payload_user = {
        "username": "abcdef",
        "password": "",
        "confirmation_password": ""
    }
    r = sign_up(payload_user)
    assert r.status_code == 400
    assert r.json()['message'] == "password is can not be empty"