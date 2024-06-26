import uuid
from sqlalchemy import Column, String, DateTime
from app.app import db

class BaseModel(db.Model):
    """ Base class for all models """
    __abstract__ = True

    uniq_id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    created_at = Column(DateTime, default=db.func.current_timestamp(), nullable=False)
    updated_at = Column(DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp(), nullable=False)

    def __repr__(self):
        return f'<BaseModel {self.uniq_id}>'
