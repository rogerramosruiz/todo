import random
import string


def random_string(length:int = 10):
    chars = string.ascii_letters + string.digits
    rand_str = ''
    for _ in range(length):
        rand_str += random.choice(chars)
    return rand_str


def gen_user():
    password = random_string()
    return  {
        'username': random_string(),
        'password': password,
        'confirmation_password': password
    }

def gen_task():
    return  {
        'name': random_string(),
    }
