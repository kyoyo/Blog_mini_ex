from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config.from_object(Config())

db = SQLAlchemy(app)


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())


# @app.route('/')
# def index():
#     return "hello world"



