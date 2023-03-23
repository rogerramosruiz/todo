import requests
from requests_auth import createuser_login


TASK_ENDPOINT = 'http://localhost:8080/api/v1/task'


def create_task(task, token):
    return requests.post(TASK_ENDPOINT, 
                        headers={
                            'Authorization': f'Bearer {token}'
                        },
                        json=task)


def get_task(id, token):    
    return requests.get(f'{TASK_ENDPOINT}/{id}', 
                        headers={
                            'Authorization': f'Bearer {token}'
                        })

def get_tasks(token):
    return requests.get(TASK_ENDPOINT, 
                        headers={
                            'Authorization': f'Bearer {token}'
                        })


def edit_task(id, task, token):
    return requests.put(f'{TASK_ENDPOINT}/{id}', 
                        headers={
                            'Authorization': f'Bearer {token}'
                        },
                        json=task)

def delete_task(id, token):
    pass
    return requests.delete(f'{TASK_ENDPOINT}/{id}', 
                        headers={
                            'Authorization': f'Bearer {token}'
                        })

