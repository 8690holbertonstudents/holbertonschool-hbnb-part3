from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from models import *
import os

db = SQLAlchemy()
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')
    engine = create_engine(SQLALCHEMY_DATABASE_URI)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    