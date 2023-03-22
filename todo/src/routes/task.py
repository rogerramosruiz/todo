from flask import Blueprint, request
import controllers.task as task_controller

task =  Blueprint('task', __name__, url_prefix='/api/v1/task')

@task.route('<int:id_user>', methods = ['GET'])
def get_tasks(id_user):
    return task_controller.get_tasks(id_user, request.args)


@task.route('', methods = ['POST'])
def create_task():
    return task_controller.create_task(request.get_json())
