from flask import Flask
from flask_cors import CORS

from routes.task import task
from config.environment import PORT, DEBUG
from db.init import intialize

# these two lines are necesary when using docker and cors
import collections
collections.Iterable = collections.abc.Iterable


app = Flask(__name__)
CORS(app)
app.register_blueprint(task)


intialize()
if __name__ == '__main__':
    app.run('0.0.0.0', PORT, DEBUG)