import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    VERSION = '0.0.1'
    SERVER_NAME = 'localhost:5000'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    # Uploads
    MAX_CONTENT_LENGTH = os.environ.get('MAX_CONTENT_LENGTH') or 25 * 1024 * 1024
    UPLOAD_DIR = os.environ.get('UPLOAD_DIR') or os.path.join(basedir, 'application/static/data')
    ALLOWED_EXTENSIONS = ['pdf', 'jpg', 'jpeg', 'png']


    LOCALES = ["en"]
    DEFAULT_TIMEZONE = "UTC"
    SESSION_COOKIE_DOMAIN = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///'
    WTF_CSRF_ENABLED = False

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')

config = {
    'development': DevelopmentConfig,
    'testing': TestConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}