from app.logger import get_logger, simple_logger
from app.core.dependencies.interfaces import MailProviderInterface

class EmailService:
    def __init__(self, mail_provider: MailProviderInterface):
        self.mail_provider = mail_provider
        self.logger = get_logger()

    @simple_logger
    def send_email(self, subject, body, to_email):
        try:
            self.mail_provider.send(subject, body, to_email)
            self.logger.info(f"Email sent to {to_email}")
        except Exception as e:
            self.logger.exception(f"Ошибка при отправке письма: {e}")
            raise