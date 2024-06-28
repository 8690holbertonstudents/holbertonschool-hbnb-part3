from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from models import *
import os

db = SQLAlchemy()
basedir = os.path.abspath(os.path.dirname(__file__))
datadir = os.path.join(basedir, 'data')
if not os.path.exists(datadir):
    os.makedirs(datadir)

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(datadir, 'development.db')
    engine = create_engine(SQLALCHEMY_DATABASE_URI)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
