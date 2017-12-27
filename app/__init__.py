from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config
from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy()
bootstrap = Bootstrap()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())

    db.init_app(app)
    bootstrap.init_app(app)

    app.config['SECRET_KEY'] = 'devkey'

    from .views import main
    app.register_blueprint(main)

    return app











