from flask import Flask
import os

def create_app(testing_config=None):
    app = Flask(__name__, instance_relative_config=True)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth)

    return app
