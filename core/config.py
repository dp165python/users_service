import logging
import os

from core.constants import APP_ENV_DEV, APP_ENV_PROD, APP_ENV_TEST


class Config:
    DB_USER = os.environ.get('DB_USER', 'postgres')
    DB_PASSWORD = os.environ.get('DB_PASSWORD', '11111111')
    DEFAULT_DB = os.environ.get('DEFAULT_DB', 'postgres')
    DB_HOST = os.environ.get('DB_HOST', 'localhost')
    DB_PORT = os.environ.get('DB_PORT', 5432)
    DEBUG = False
    HOST = '127.0.0.1'
    LOG_LEVEL = logging.INFO
    TOKEN = os.environ.get('TOKEN', None)
    DB_NAME = os.environ.get('DB_NAME', 'users')
    DB_URI = 'postgresql://{user}:{password}@{host}:{port}/{db_name}'


class TestConfig(Config):
    DEBUG = True
    TESTING = True
    DB_NAME = os.environ.get('DB_NAME', 'test_users')
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class ProdConfig(Config):
    LOG_LEVEL = logging.ERROR


class DevConfig(Config):
    DEBUG = True


def runtime_config():
    env = os.environ.get("APP_ENV", APP_ENV_DEV).strip().lower()
    if env == APP_ENV_PROD:
        return ProdConfig
    elif env == APP_ENV_TEST:
        return TestConfig

    return DevConfig
