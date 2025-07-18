# GitHub Webhook Listener

Небольшой pet-проект для обработки GitHub webhook'ов, отправки уведомлений на email и отображения последних коммитов через веб-интерфейс.

## Стек технологий

- **Python 3.10+**
- **Flask**
- **Flask-Mail**
- **Flask-SQLAlchemy**
- **WTForms**
- **SQLite**
- **HTML + CSS (без фреймворков)**

## Что делает проект

- Принимает push и merge события с GitHub через webhook
- Отправляет email с деталями коммита
- Сохраняет данные в SQLite
- Показывает коммиты на дашборде (`/dashboard`)

## Безопасность

Для верификации запросов используется простая проверка подписи с помощью HMAC:

```python
X-Hub-Signature-256 → сравнивается с HMAC SHA-256
```

Ключ хранится в .env как WEBHOOK_SECRET.

Важно: проект работает только локально и не рассчитан на прод. Уровень безопасности минимальный и подходит только для обучающих целей.

## Архитектура

Проект построен по MVC + DI (Dependency Injection) с разделением ответственности:

```csharp
app/
├── controllers/         # Роуты (webhook, dashboard)
├── services/            # Бизнес-логика (email, обработка событий)
├── models/              # SQLAlchemy модели
├── templates/           # Jinja2 шаблоны
├── static/              # CSS/JS
├── core/
│   └── dependencies/    # DI контейнер и интерфейсы
```

## Как запустить

1. Клонируем репозиторий:

```bash
git clone https://github.com/yourusername/webhook_listener.git
cd webhook_listener
```

2. Создаем .env файл:

```ini
SECRET_KEY=your_flask_secret_key

# SMTP настройки
MAIL_USERNAME=your_email@example.com
MAIL_PASSWORD=your_email_password
MAIL_SERVER=smtp.example.com
MAIL_PORT=587
MAIL_USE_TLS=True

# Webhook-секрет
WEBHOOK_SECRET=your_webhook_secret

# Email получателя (если не задан — будет использован MAIL_USERNAME)
NOTIFY_EMAIL=your_email@example.com
```

3. Установка зависимостей:

```bash
pip install -r requirements.txt
```

4. Создание базы данных:

```bash
python create_db.py
```

5. Запуск приложения:

```bash
python run.py
```

6. Прокидываем внешний URL с помощью LocalTunnel или ngrok:

```bash
lt --port 5000
```

7. Нужно указать подобный URL в GitHub webhook'ах - https://your-url/webhook

## Email

Письмо содержит:

Название репозитория

Сообщение коммита

Ссылку на сам commit

Отправляется через Flask-Mail по адресу из NOTIFY_EMAIL или MAIL_USERNAME.

## Дашборд

Находится по ссылке http://localhost:5000/dashboard чтобы видеть последние коммиты.

## TODO / Возможные улучшения

- Авторизация и логин

- Поддержка нескольких репозиториев

- Админка для управления хуками

- Отображение diff'ов или файлов в коммите

## Заметки

Проект предназначен для обучения и демонстрации архитектурных принципов.

Не рекомендуется использовать как есть в продакшене без доработок (безопасность, деплой, хостинг, TLS и т.п.).