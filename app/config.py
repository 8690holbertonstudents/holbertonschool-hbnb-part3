import os
import app
from flask import SQLAlchemy


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


app.config.from_object('config.DevelopmentConfig' if \
    os.environ.get('ENV') == 'development' else 'config.ProductionConfig')

db = SQLAlchemy(app)
