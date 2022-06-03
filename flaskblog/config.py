import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')

    MAIL_SERVER= 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    # app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
    # app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
    MAIL_USERNAME = 'steffy.inexture@gmail.com'
    MAIL_PASSWORD = 'steffy!p@7069214086'