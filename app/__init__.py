from flask import Flask
import os

def create_app(testing_config=None):
    app = Flask(__name__, instance_relative_config=True)

    from .views import views


    app.register_blueprint(views, url_prefix='/')

    return app
