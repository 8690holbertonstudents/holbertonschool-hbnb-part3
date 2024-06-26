"""
Python module for amenity class
"""
from models.base_model import BaseModel
from models import db


class Amenity(BaseModel):
    """
    Defines the Amenity class that inherits from BaseModel
    """
    __tablename__ = 'amenities'
    name = db.Column(db.String(128),
                     nullable=False)
