import os
from dotenv import load_dotenv
from distutils.util import strtobool
from enum import Enum
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin

load_dotenv()

APP_SECRET_KEY = os.environ.get('APP_SECRET_KEY', 'secret')
DB_ECHO = strtobool(os.environ.get('DB_ECHO', 'False'))
DB_TRACK_MODIFICATIONS = strtobool(
    os.environ.get('DB_TRACK_MODIFICATIONS', 'False'))
DATABASE_URL = os.environ.get(
    'DATABASE_URL', 'sqlite:///polynomial_evaluator.db')
TEST_DATABASE_URL = os.environ.get(
    'TEST_DATABASE_URL', 'sqlite:///polynomial_evaluator_test.db')


class Config:
    TESTING = True
    DEBUG = True

    SQLALCHEMY_ECHO = DB_ECHO
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = DB_TRACK_MODIFICATIONS

    # Secret key for signing cookies
    SECRET_KEY = APP_SECRET_KEY

    # Api config
    APISPEC_SPEC = APISpec(
        title='Simple Polynomial Evaluator',
        version='1.0.0',
        openapi_version='2.0.2',
        plugins=[MarshmallowPlugin()]
    )
    APISPEC_SWAGGER_URL = '/swagger/'


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    TESTING = False


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = TEST_DATABASE_URL


class ConfigNames(Enum):
    PRODUCTION = ProductionConfig
    DEVELOPMENT = DevelopmentConfig
    TESTING = TestingConfig

    @staticmethod
    def from_str(label: str):
        label = label.upper()
        return ConfigNames[label]
