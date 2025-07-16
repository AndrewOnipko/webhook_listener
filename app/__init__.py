from flask import Flask
from flask_mail import Mail
from config import Config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
mail = Mail()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    mail.init_app(app)

    from .routes.routes import webhook_bp
    app.register_blueprint(webhook_bp)

    return app