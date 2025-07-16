import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev")
    
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME") 
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD") 

    SQLALCHEMY_DATABASE_URI = "sqlite:///instance/webhook.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False