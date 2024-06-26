import uuid
from app.app import db

class BaseModel(db.Model):
    """ Base class for all models """
    __abstract__ = True

    uniq_id = db.Column(db.String(36),
                        primary_key=True, default=lambda: str(uuid.uuid4()))
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, onupdate=db.func.current_timestamp())


"""Convention pour debugger"""
def __repr__(self):
    return f'<BaseModel {self.uniq_id}>'
