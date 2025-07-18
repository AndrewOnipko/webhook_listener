from app.services.email_service import EmailService
from app.core.dependencies.mail_provider import FlaskMailProvider

class Container:
    def __init__(self):
        self._email_service = None

    @property
    def email_service(self):
        if self._email_service is None:
            self._email_service = EmailService(mail_provider=FlaskMailProvider())
        return self._email_service

container = Container()