
class Config(object):
    DEBUG = True
    DEVELOPMENT = True
    SECRET_KEY = "my-secret-key"
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
    JWT_ALG = "HS256"
