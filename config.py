import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    EMAIL_URL = os.environ.get('BIO_DLF_EMAIL_URL')
    EMAIL_KEY = os.environ.get('BIO_DLF_EMAIL_KEY')
    EMAIL_FROM = os.environ.get('BIO_DLF_EMAIL_FROM')
    EMAIL_TO = os.environ.get('BIO_DLF_EMAIL_TO')
    SECRET_KEY = os.environ.get('BIO_DLF_SECRET_KEY')

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    pass

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
