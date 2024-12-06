from flask import Flask
from app.routes.tracker import traker_bp


def register_blueprints(app: Flask) -> None:
    app.register_blueprint(traker_bp)

