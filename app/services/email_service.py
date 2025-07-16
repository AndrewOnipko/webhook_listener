from flask_mail import Message
from flask import current_app
from app import mail
from app.logger import get_logger, simple_logger

class EmailService:
    def __init__(self):
        self.logger = get_logger()
    
    
    @simple_logger
    def send_email(self, subject, body, to_email):
        try:
            msg = Message(
                subject=subject,
                sender=current_app.config["MAIL_USERNAME"],
                recipients=[to_email],
                body=body
            )
            mail.send(msg)
            self.logger.info(f"Email sent to {to_email}")
        except Exception as e:
            self.logger.exception(f"Ошибка при отправке письма: {e}")
            raise