"""
Python module manage config app
"""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from dotenv import load_dotenv
from models import *
import psycopg2
import os

load_dotenv()

db = SQLAlchemy()

# Generate and force directory for SQLite db
basedir = os.path.abspath(os.path.dirname(__file__))
datadir = os.path.join(basedir, 'data')
if not os.path.exists(datadir):
    os.makedirs(datadir)


class Config:
    """
    Define Config class with development environment (Sqlite)
    or production environment (Postgresql)
    """
    if os.environ.get('FLASK_ENV') == 'production':
        usr = os.environ.get('USERNAME')
        pwd = os.environ.get('PASSWORD')
        db_host = os.environ.get('DB_HOST')
        db_port = os.environ.get('DB_PORT')
        db_name = os.environ.get('DB_NAME')

        SQLALCHEMY_DATABASE_URI = f'postgresql://{usr}:{pwd}@{db_host}:{db_port}/{db_name}'
        engine = create_engine(SQLALCHEMY_DATABASE_URI)
        SQLALCHEMY_TRACK_MODIFICATIONS = False

    elif os.environ.get('FLASK_ENV') == 'development':
        SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
            os.path.join(datadir, 'development.db')
        engine = create_engine(SQLALCHEMY_DATABASE_URI)
        SQLALCHEMY_TRACK_MODIFICATIONS = False
