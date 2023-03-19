import requests
import random
import string

ENDPOINT = 'http://localhost:3000/api/v1'

def sign_up(json_paload):
    return requests.post(f'{ENDPOINT}/signup', json=json_paload)

def login(json_paload):
    return requests.post(f'{ENDPOINT}/login', json=json_paload)

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