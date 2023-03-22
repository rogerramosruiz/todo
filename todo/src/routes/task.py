from flask import Blueprint, request
import controllers.task as task_controller

task =  Blueprint('task', __name__, url_prefix='/api/v1/task')

@task.route('<int:id_user>', methods = ['GET'])
def get_tasks(id_user):
    return task_controller.get_tasks(id_user, request.args)

@task.route('one/<int:id>', methods = ['GET'])
def get_task(id):
    return task_controller.get_task(id)

@task.route('', methods = ['POST'])
def create_task():
    return task_controller.create_task(request.get_json())

@task.route('/<int:id>', methods=["PUT"])
def edit_task(id):
    return task_controller.edit_task(id, request.get_json())

@task.route('/<int:id>', methods= ["DELETE"])
def delete_task(id):
    return task_controller.delete_task(id)