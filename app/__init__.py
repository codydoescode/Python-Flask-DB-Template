from flask import Flask
from .routes.main import main_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(main_bp)
    return app
