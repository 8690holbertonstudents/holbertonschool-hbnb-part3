"""
Python module for country class
"""
from config import db


class Country(db.Model):
    """
    Defines the Country class that inherits from db.Model
    """
    __tablename__ = 'countries'
    # Fields definition
    name = db.Column(db.String(128),
                     unique=True,
                     nullable=False)
    code = db.Column(db.String(2),
                     primary_key=True)
    # 1 to many relationship with City
    cities = db.relationship('City',
                             back_populates='country')

    def __repr__(self):
        return f'<Country {self.name}>'

    """
    def to_dict(self):
        """
    """
        result = {}
        for key, value in self.__dict__.items():
            result[key] = value
        return result
    """
