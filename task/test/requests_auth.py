import requests
from helpers import gen_user

AUTH_ENDPOINT = 'http://localhost:3000/api/v1'

def sign_up(json_payload):
    return requests.post(f'{AUTH_ENDPOINT}/signup', json=json_payload)


def login(json_payload):
    return requests.post(f'{AUTH_ENDPOINT}/login', json=json_payload)

def createuser_login():
    user = gen_user()
    sign_up(user)
    user.pop('confirmation_password')
    r = login(user)
    return r.json()['access_token']