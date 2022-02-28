
class Config(object):
    DEBUG = False
    DEVELOPMENT = False
    SECRET_KEY = "my-secret-key"
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
    JWT_ALG = "HS256"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Testing(Config):
    DEBUG = True
    TESTING = True


class Production(Config):
    DEBUG = False
    DEVELOPMENT = False
