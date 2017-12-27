from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from .views import main



app = Flask(__name__)
app.config.from_object(Config())

db = SQLAlchemy(app)

app.register_blueprint(main)







