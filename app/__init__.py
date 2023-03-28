from flask import Flask
from config import Config

def creste_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    from .main import bp as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    return app


app = creste_app()
