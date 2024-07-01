"""
Python module for amenity class
"""
from .base_model import BaseModel
# from .place_amenity import PlaceAmenity
from config import db


class Amenity(BaseModel):
    """
    Defines the Amenity class that inherits from BaseModel
    """
    __tablename__ = 'amenities'
    # Fields definition
    name = db.Column(db.String(128),
                     nullable=False)
    """
    # Many to Many relationship with Place
    place_amenities = db.relationship('PlaceAmenity',
                                      back_populates='amenity')
    """

    def __repr__(self):
        return f'<Amenity {self.name}>'
