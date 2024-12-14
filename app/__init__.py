from flask import Flask
from .config import Config
from .extensions import db, migrate, login_manager

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # Register blueprints
    from .routes import auth, tracker, api
    app.register_blueprint(auth.bp)
    app.register_blueprint(tracker.bp)
    app.register_blueprint(api.bp)

    return app
