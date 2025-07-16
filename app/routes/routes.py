from flask import Blueprint, request, jsonify, render_template, current_app, abort
from app.services.email_service import EmailService
from app.handlers.push_event_handler import PushEventHandler
from app.logger import simple_logger
from app.models import PushEvent
import hmac
import hashlib

webhook_bp = Blueprint("webhook", __name__)

def verify_signature(request):
    secret = current_app.config['WEBHOOK_SECRET']
    if not secret:
        return False

    signature = request.headers.get('X-Hub-Signature-256')
    if signature is None:
        return False

    sha_name, signature = signature.split('=')
    if sha_name != 'sha256':
        return False

    mac = hmac.new(secret.encode(), msg=request.data, digestmod=hashlib.sha256)
    expected = mac.hexdigest()
    return hmac.compare_digest(expected, signature)
                               

@simple_logger
@webhook_bp.route("/test-email")
def send_test_email():
    email_service = EmailService()
    email_service.send_email("Тест", "Это тестовое письмо", "nekoc528@gmail.com")
    return "Письмо отправлено"

@simple_logger
@webhook_bp.route("/webhook", methods=["POST"])
def push_webhook():
    if not verify_signature(request):
        abort(403)
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