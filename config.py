import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'FJKkdjfk785dh67r87GUkj74j5hj')

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:////temp/test.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False