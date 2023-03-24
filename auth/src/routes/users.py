from flask import Blueprint, request
import controllers.users

users = Blueprint('users', __name__, url_prefix='/api/v1/auth')

@users.route('/signup', methods = ['POST'])
def signup():
    return controllers.users.signup(request.get_json())