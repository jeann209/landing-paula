from flask import Flask
from backend.config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    from .main.routes import main
    app.register_blueprint(main)

    return app
