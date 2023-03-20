from flask import Blueprint, request
import controllers.auth
from middlewares.auth_middleware import token_verifier
auth = Blueprint('auth',__name__, url_prefix='/api/v1')

@auth.route('/login', methods = ['POST'])
def login():
    return controllers.auth.login(request.get_json())

# logout
# deleting form reddis cash

@auth.route('/token', methods = ['GET'])
@token_verifier
def token():
    return controllers.auth.token()