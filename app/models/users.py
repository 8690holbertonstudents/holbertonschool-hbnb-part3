from .BaseModel import BaseModel
from config import db

class User(BaseModel):
    """ User class """
    __tablename__ = 'users'

    email = db.Column(db.String(100), unique=True, nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'
