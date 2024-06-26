from models.base_model import BaseModel
from sqlalchemy import Column, String

class User(BaseModel):
    """ User class """
    __tablename__ = 'users'

    email = Column(String(100), unique=True, nullable=False)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'
