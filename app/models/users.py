"""
Python module for user model
"""
from models.base_model import BaseModel
from models import db


class User(BaseModel):
    """
    Defines the User model class inheriting from BaseModel
    """
    __tablename__ = 'users'
    email = db.Column(db.String(128),
                      unique=True,
                      nullable=False)
    first_name = db.Column(db.String(128),
                           nullable=False)
    last_name = db.Column(db.String(128),
                          nullable=False)
