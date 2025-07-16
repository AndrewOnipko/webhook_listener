from flask import Blueprint
from app.services.email_service import EmailService

webhook_bp = Blueprint("webhook", __name__)

@webhook_bp.route("/test-email")
def send_test_email():
    email_service = EmailService()
    email_service.send_email("Тест", "Это тестовое письмо", "nekoc528@gmail.com")
    return "Письмо отправлено"