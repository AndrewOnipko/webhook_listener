from app.models.push_event import PushEvent
from app.core.dependencies.container import container
from app.models.push_event import PushEvent
from flask import current_app

class WebhookService:
    def __init__(self, email_service=None):
        self.email_service = email_service or container.email_service

    def handle_push(self, payload):
        commit = payload.get("head_commit", {})
        msg = commit.get("message", "Без сообщения")
        url = commit.get("url", "Без ссылки")
        repo = payload.get("repository", {}).get("full_name", "Неизвестный репозиторий")

        subject = f"Новый коммит в {repo}"
        body = f"Сообщение: {msg}\nСсылка: {url}"

        
        to_email = current_app.config.get("NOTIFY_EMAIL") or current_app.config.get("MAIL_USERNAME")
        self.email_service.send_email(subject, body, to_email)
        PushEvent.create(repository=repo, message=msg, url=url)