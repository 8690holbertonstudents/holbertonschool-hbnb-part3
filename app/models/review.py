"""
Python module for review class
"""
from models.base_model import BaseModel
from models import db


class Review(BaseModel):
    """
    Defines the Review class that inherits from BaseModel
    """
    __tablename__ = 'reviews'
    user_id = db.Column(db.String(36),
                        db.ForeignKey('users.id'),
                        nullable=False)
    place_id = db.Column(db.String(36),
                         db.ForeignKey('places.id'),
                         nullable=False)
    rating = db.Column(db.Integer,
                       nullable=False)
    comment = db.Column(db.String(1024),
                        nullable=False)
