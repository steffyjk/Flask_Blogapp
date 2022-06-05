import os

from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
    print(f"************ {os.environ.get('DATABASE_URL')}")
    MAIL_SERVER= 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
    Host = os.environ.get('Host')
    Database= os.environ.get('Database')
    User= os.environ.get('User')
    Port= os.environ.get('Port')
    Password= os.environ.get('Password')
    # URI= os.environ.get('URI')


# DATABASE_URI=postgresql://postgres:harsh2022@localhost:5432/blogapp