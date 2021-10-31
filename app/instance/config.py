import os


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY")

    MAX_CONTENT_LENGTH = 1024 * 1024


class DevelopmentConfig(Config):
    ENV = 'development'
    DEBUG = True


class ProductionConfig(Config):
    ENV = 'production'
