"""
Python module for amenity class
"""
from .base_model import BaseModel
from config import db


class Amenity(BaseModel):
    """
    Defines the Amenity class that inherits from BaseModel
    """
    __tablename__ = 'amenities'
    # Fields definition
    name = db.Column(db.String(128),
                     nullable=False)
    # Many to Many relationship with Place
    places = db.relationship('Place',
                             secondary='place_amenity',
                             back_populates='amenities')

    def __repr__(self):
        return f'<Amenity {self.name}>'
