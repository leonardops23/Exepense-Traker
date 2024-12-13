from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(testing_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config['SECRET_KEY'] = 'asdjfklj!@!2ssdkj'

    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth)

    return app
