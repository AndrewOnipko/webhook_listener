from flask_mail import Message
from flask import current_app
from app import mail
from app.core.dependencies.interfaces import MailProviderInterface

class FlaskMailProvider(MailProviderInterface):
    def send(self, subject, body, to_email):
        msg = Message(
            subject=subject,
            sender=current_app.config["MAIL_USERNAME"],
            recipients=[to_email],
            body=body
        )
        mail.send(msg)
