from flask import Flask
from routes.task import task

from config.environment import PORT, DEBUG
from db.init import intialize

app = Flask(__name__)
app.register_blueprint(task)


if __name__ == '__main__':
    intialize()
    app.run('0.0.0.0', PORT, DEBUG)