import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev")
    WEBHOOK_SECRET = os.environ.get('WEBHOOK_SECRET')
    basedir = os.path.abspath(os.path.dirname(__file__))
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME") 
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD") 
    NOTIFY_EMAIL = os.environ.get("NOTIFY_EMAIL", os.environ.get("MAIL_USERNAME"))


    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(basedir, 'instance', 'webhook.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #Строка для проверки коммита22as