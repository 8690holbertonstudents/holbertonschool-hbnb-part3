from config import Config, db
from sqlalchemy.orm import sessionmaker
import datetime

Session = sessionmaker(bind=Config.engine)
session = Session()

class DataManager:
    def save(entity):
        try:
            session.add(entity)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def read(entity):
        result = {}
        for key, value in entity.__dict__.items():
            if key != '_sa_instance_state':
                if isinstance(value, datetime.datetime):
                    result[key] = value.isoformat()
                else:
                    result[key] = value
        return result

    def update(entity, updates):
        try:
            entity = session.merge(entity)
            for key, value in updates.items():
                if hasattr(entity, key):
                    setattr(entity, key, value)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def delete(entity):
        try:
            session.delete(entity)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
