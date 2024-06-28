"""
Python module for city class
"""
from config import db
from .base_model import BaseModel


class City(BaseModel):
    """
    Defines the City class that inherits from BaseModel
    """
    __tablename__ = 'cities'
    name = db.Column(db.String(128),
                     nullable=False)
    country_code = db.Column(db.String(2),
                             db.ForeignKey('countries.code'),
                             nullable=False)
