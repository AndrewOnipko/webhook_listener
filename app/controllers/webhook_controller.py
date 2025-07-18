from flask import Blueprint, request, jsonify, current_app, abort
import hmac, hashlib
from app.services.webhook_service import WebhookService
from app.logger import simple_logger

webhook_bp = Blueprint("webhook", __name__)

def verify_signature(request):
    secret = current_app.config['WEBHOOK_SECRET']
    signature = request.headers.get('X-Hub-Signature-256')
    if not signature:
        return False

    sha_name, signature = signature.split('=')
    if sha_name != 'sha256':
        return False

    mac = hmac.new(secret.encode(), msg=request.data, digestmod=hashlib.sha256)
    return hmac.compare_digest(mac.hexdigest(), signature)

@webhook_bp.route("/webhook", methods=["POST"])
@simple_logger
def handle_webhook():
    if not verify_signature(request):
        abort(403)

    event_type = request.headers.get("X-GitHub-Event")
    payload = request.get_json()

    if event_type == 'push':
        WebhookService().handle_push(payload)

    return jsonify({"status": "ok"})