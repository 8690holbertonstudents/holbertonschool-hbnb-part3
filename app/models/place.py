"""
Python module for place class
"""
from models.base_model import BaseModel
from models import db


class Place(BaseModel):
    """
    Defines the Place class that inherits from BaseModel
    """
    __tablename__ = 'places'
    name = db.Column(db.String(128),
                     nullable=False)
    description = db.Column(db.String(1024),
                            nullable=False)
    adress = db.Column(db.String(256),
                       nullable=False)
    city_id = db.Column(db.String(36),
                        db.ForeignKey('cities.id'),
                        nullable=False)
    latitude = db.Column(db.Float,
                         nullable=False)
    longitude = db.Column(db.Float,
                          nullable=False)
    host_id = db.Column(db.String(36),
                        db.ForeignKey('users.id'),
                        nullable=False)
    num_rooms = db.Column(db.Integer,
                          nullable=False)
    num_bathrooms = db.Column(db.Integer,
                              nullable=False)
    price_per_night = db.Column(db.Float,
                                nullable=False)
    max_guests = db.Column(db.Integer,
                           nullable=False)
