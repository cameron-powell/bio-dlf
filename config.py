import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('BIO_DLF_SECRET_KEY')
    MAIL_RECEIVER = os.environ.get('BIO_DLF_MAIL_RECEIVER')

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('BIO_DLF_MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('BIO_DLF_MAIL_PASSWORD')


class ProductionConfig(Config):
    pass

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
