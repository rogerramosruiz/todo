from requests_task import get_tasks, get_task, create_task, edit_task, delete_task
from requests_auth import createuser_login
from helpers import gen_task


def tests_create_task():
    token = createuser_login()
    task = gen_task()
    r = create_task(task, token)

    assert r.status_code == 201
    assert 'id' in r.json()
    
    id = r.json()['id']
    r = get_task(id, token)
    task_json = r.json()

    assert task_json['name'] == task['name']
    assert task_json['done'] == False


def test_get_tasks():
    n = 5
    token = createuser_login()
    tasks = []

    for _ in range(n):
        task = gen_task()
        tasks.append(task)
        create_task(task, token)

    r = get_tasks(token)
    tasks_resp = r.json()

    assert r.status_code == 200
    assert n == len(tasks_resp)
    for t, tr in zip(tasks, tasks_resp):
        assert t['name'] == tr['name'] 
        assert tr['done'] == False


def test_edit_task():
    token = createuser_login()
    task = gen_task()
    id = create_task(task, token).json()['id']
    task['done'] = True
    task['name'] = 'edited task'
    r = edit_task(id, task, token)

    assert r.status_code == 202
    assert r.json()['message'] =='Success'

    task_json = get_task(id, token).json()
    assert task_json['done'] == task['done']
    assert task_json['name'] == task['name']

def test_delete_task():
    token = createuser_login()
    task = gen_task()
    id = create_task(task, token).json()['id']
    
    r = delete_task(id, token)

    assert r.status_code == 202
    assert r.json()['message'] == 'Success'

    r = get_task(id, token)
    assert r.status_code == 404
    assert r.json()['message'] == 'Task not found'


