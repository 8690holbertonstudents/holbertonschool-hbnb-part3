from persistence.ipersistencemanager import IPersistenceManager
from app.app import db

class DataManager(IPersistenceManager):

    def __init__(self, flag):
        self.session = db.session

    def save(self, entity):
        """
        Methdod used to save data(entity) into a JSON file
        """
        self.session.add(entity)
        self.session.commit()
