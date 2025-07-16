from flask import Blueprint, request, jsonify, render_template
from app.services.email_service import EmailService
from app.handlers.push_event_handler import PushEventHandler
from app.logger import simple_logger
from app.models import PushEvent

webhook_bp = Blueprint("webhook", __name__)

@simple_logger
@webhook_bp.route("/test-email")
def send_test_email():
    email_service = EmailService()
    email_service.send_email("Тест", "Это тестовое письмо", "nekoc528@gmail.com")
    return "Письмо отправлено"

@simple_logger
@webhook_bp.route("/webhook", methods=["POST"])
def push_webhook():
    event_type = request.headers.get("X-GitHub-Event")

    if event_type == 'push':
        payload = request.get_json()
        email_service = EmailService()
        handler = PushEventHandler(email_service)
        handler.handle(payload)

    return jsonify({"status": "ok"})


@simple_logger
@webhook_bp.route("/dashboard", methods=["GET"])
def dashboard():
    commits = PushEvent.query.order_by(PushEvent.timestamp.desc()).all()
    return render_template("dashboard.html", commits=commits)