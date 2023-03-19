from flask import Flask
from config.environment import PORT, DEBUG
from routes.users import users
from routes.auth import auth
app = Flask(__name__)

@app.route('/', methods=['GET'])
def ping():
    return {'message': 'ok'}

app.register_blueprint(users)
app.register_blueprint(auth)

if __name__ == '__main__':
    app.run('0.0.0.0', PORT, debug=DEBUG)