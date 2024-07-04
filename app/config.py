from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import create_engine
from dotenv import load_dotenv
from models import *
import os


db = SQLAlchemy()
basedir = os.path.abspath(os.path.dirname(__file__))
datadir = os.path.join(basedir, 'data')
if not os.path.exists(datadir):
    os.makedirs(datadir)


class Config:
    if os.environ.get('FLASK_ENV') == 'production':
        load_dotenv('.env.prod')
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
        engine = create_engine(SQLALCHEMY_DATABASE_URI)
        SQLALCHEMY_TRACK_MODIFICATIONS = False
    else:
        load_dotenv('.env.dev')
        SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
            os.path.join(datadir, 'development.db')
        engine = create_engine(SQLALCHEMY_DATABASE_URI)
        SQLALCHEMY_TRACK_MODIFICATIONS = False
