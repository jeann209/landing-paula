from decouple import config


class Config:
    SECRET_KEY = config('SECRET_KEY', default='dev-secret-key')
    DEBUG = config('DEBUG', default=True, cast=bool)
