from flask import Flask
from config.environment import PORT, DEBUG
app = Flask(__name__)



if __name__ == '__main__':
    app.run('0.0.0.0', PORT, DEBUG)