"""
Python module for defining the base model
"""
import datetime
from sqlalchemy.dialects.postgresql import UUID
from models import db
import uuid


class BaseModel(db.Model):
    """
    Defines the subclass BaseModel that inherits from db.Model
    """
    __abstract__ = True
    id = db.Column(UUID(as_uuid=True),
                   primary_key=True,
                   default=uuid.uuid4,
                   unique=True,
                   nullable=False)
    created_at = db.Column(db.DateTime,
                           default=db.func.current_timestamp(),
                           nullable=False)
    updated_at = db.Column(db.DateTime,
                           default=db.func.current_timestamp(),
                           onupdate=db.func.current_timestamp(),
                           nullable=False)

    def to_dict(self):
        """
        """
        result = {}
        for key, value in self.__dict__.items():
            if isinstance(value, datetime.datetime):
                result[key] = value.isoformat()
            else:
                result[key] = value
        return result
