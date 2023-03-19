from flask import Blueprint, request
import controllers.auth

auth = Blueprint('auth',__name__, url_prefix='/api/v1')

@auth.route('/login', methods = ['POST'])
def login():
    return controllers.auth.login(request.get_json())

@auth.route('/token', methods = ['POST'])
def token():
    return controllers.auth.token()