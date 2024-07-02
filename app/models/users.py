"""
Python module for User class
"""
from .base_model import BaseModel
from flask_bcrypt import bcrypt
from config import db


class User(BaseModel):
    """
    Defines User class that inherits from BaseModel
    """
    __tablename__ = 'users'
    # Fields definition
    email = db.Column(db.String(100), unique=True, nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    # JWT secure authentification
    password_hash = db.Column(db.String(128))

    is_admin = db.Column(db.Boolean,
                         default=False)
    # 1 to 1 relationship with Place
    place = db.relationship('Place',
                            uselist=False,
                            back_populates='host')

    # 1 to many relationship with Review
    reviews = db.relationship('Review', back_populates='user')

    def __repr__(self):
        return f'<User {self.email}>'

    def set_password(self, password):
        """
        Sets the password hash for the user
        """
        self.password_hash = bcrypt.generate_password_hash(
            password).decode('utf-8')

    def check_password(self, password):
        """
        Checks if given password matches the user's password hash
        """
        return bcrypt.check_password_hash(self.password_hash, password)
