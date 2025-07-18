from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from config import Config

db = SQLAlchemy()
mail = Mail()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    mail.init_app(app)

    from app.controllers.webhook_controller import webhook_bp
    from app.controllers.dashboard_controller import dashboard_bp

    app.register_blueprint(webhook_bp)
    app.register_blueprint(dashboard_bp)

    return app