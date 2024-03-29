import requests

ENDPOINT = 'http://localhost/api/v1/auth'
def sign_up(json_paload):
    return requests.post(f'{ENDPOINT}/signup', json=json_paload)

def login(json_paload):
    return requests.post(f'{ENDPOINT}/login', json=json_paload)

def refresh_token(token):
    return requests.get(f'{ENDPOINT}/token', headers={
        'Authorization': f'Bearer {token}'
    })

def logout(token):
    return requests.delete(f'{ENDPOINT}/logout', headers={
        'Authorization': f'Bearer {token}'
    })

def verication_token(token):
    return requests.get(f'{ENDPOINT}/verify', headers={
        'Authorization': f'Bearer {token}'
    })