from flask import Blueprint, request, g
import controllers.task as task_controller
from middlewares.auth_middleware import token_verifier

task =  Blueprint('task', __name__, url_prefix='/api/v1/task')
@task.route('', methods = ['GET'])
@token_verifier
def get_tasks():
    return task_controller.get_tasks(g.id_user, request.args)

@task.route('/<int:id>', methods = ['GET'])
@token_verifier
def get_task(id):
    return task_controller.get_task(g.id_user, id)

@task.route('', methods = ['POST'])
@token_verifier
def create_task():
    return task_controller.create_task(g.id_user, request.get_json())

@task.route('/<int:id>', methods=['PUT'])
@token_verifier
def edit_task(id):
    return task_controller.edit_task(g.id_user, id, request.get_json())

@task.route('/<int:id>', methods= ["DELETE"])
@token_verifier
def delete_task(id):
    return task_controller.delete_task(g.id_user, id)