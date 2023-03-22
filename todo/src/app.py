from flask import Flask
from config.environment import PORT, DEBUG
from routes.task import task

app = Flask(__name__)
app.register_blueprint(task)


if __name__ == '__main__':
    app.run('0.0.0.0', PORT, DEBUG)