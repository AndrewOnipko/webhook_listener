from flask import Flask
from flask_mail import Mail
from config import Config

mail = Mail()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    mail.init_app(app)

    from .routes.routes import webhook_bp
    app.register_blueprint(webhook_bp)

    return app