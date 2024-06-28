"""
Python module for city class
"""
from .base_model import BaseModel
from config import db


class City(BaseModel):
    """
    Defines the City class that inherits from BaseModel
    """
    __tablename__ = 'cities'
    name = db.Column(db.String(128),
                     nullable=False)
    country_code = db.Column(db.String(2),
                             db.ForeignKey('country_code'),
                             nullable=False)
