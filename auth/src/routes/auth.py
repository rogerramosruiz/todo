from flask import Blueprint, request
import controllers.auth
from middlewares.auth_middleware import refresh_token_verifier
auth = Blueprint('auth',__name__, url_prefix='/api/v1')

@auth.route('/login', methods = ['POST'])
def login():
    return controllers.auth.login(request.get_json())

@auth.route('/logout', methods = ['DELETE'])
@refresh_token_verifier
def logout():
    return controllers.auth.logout()

@auth.route('/token', methods = ['GET'])
@refresh_token_verifier
def token():
    return controllers.auth.token()

@auth.route('verify', methods = ['GET'])
def verify():
    return controllers.auth.verify(request.headers)