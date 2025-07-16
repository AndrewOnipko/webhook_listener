from app import db
from app.models import PushEvent

class PushEventHandler:
    def __init__(self, email_service):
        self.email_service = email_service

    def handle(self, payload):
        commit = payload.get("head_commit", {})
        commit_msg = commit.get("message", "Без сообщения")
        commit_url = commit.get("url", "Без ссылки")
        repo_name = payload.get("repository", {}).get("full_name", "Неизвестный репозиторий")

        subject = f"Новый коммит в {repo_name}"
        body = f"Сообщение: {commit_msg}\nСсылка: {commit_url}"

        self.email_service.send_email(subject, body, "nekoc528@gmail.com")
        event = PushEvent(
            repository=repo_name,
            message=commit_msg,
            url=commit_url
        )
        db.session.add(event)
        db.session.commit()

