"""
Python module for PlaceAmenity class
"""
from config import db


class PlaceAmenity(db.Model):
    """
    Defines PlaceAmenity class that represents
    the many-to-many relationship
    """
    __tablename__ = 'place_amenity'
    place_id = db.Column(db.String(36),
                         db.ForeignKey('places.id'),
                         primary_key=True)
    amenity_id = db.Column(db.String(36),
                           db.ForeignKey('amenities.id'),
                           primary_key=True)
    additional_data = db.Column(db.String(128))
