from flask import Flask
from flask_cors import CORS

from config.environment import PORT, DEBUG
from routes.users import users
from routes.auth import auth
from db.init import intialize

# these two lines are necesary when using docker and cors
import collections
collections.Iterable = collections.abc.Iterable


app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def ping():
    return 'ok'

app.register_blueprint(users)
app.register_blueprint(auth)

intialize()

if __name__ == '__main__':
    app.run('0.0.0.0', PORT, debug=DEBUG)