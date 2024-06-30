"""
Python module for User class
"""
from .base_model import BaseModel
from config import db


class User(BaseModel):
    """
    Defines User class that inherits from BaseModel
    """
    __tablename__ = 'users'
    # Fields definition
    email = db.Column(db.String(100),
                      unique=True,
                      nullable=False)
    first_name = db.Column(db.String(100),
                           nullable=False)
    last_name = db.Column(db.String(100),
                          nullable=False)
    # 1 to 1 relationship with Place
    place = db.relationship('Place',
                            back_populates='host')
    # 1 to many relationship with Review
    reviews = db.relationship('Review',
                              back_populates='user')

    def __repr__(self):
        return f'<User {self.email}>'
