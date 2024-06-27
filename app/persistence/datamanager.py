from config import db

class DataManager:

    def __init__(self):
        self.session = db.session

    def save(self, entity):
        self.session.add(entity)
        self.session.commit()
