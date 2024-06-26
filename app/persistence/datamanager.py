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

"""
    def get(self, entity, id):

        Method used to get data(entity) from a JSON file

        try:
            with open(self.file_path, 'r', encoding='UTF-8') as f:
                data = json.load(f)
                for item in data:
                    if item["uniq_id"] == id:
                        return item
        except FileNotFoundError:
            pass
"""
"""
    def delete(self, entity, id):

        Method used to delete data(entity) from a JSON file


        try:
            with open(self.file_path, 'r', encoding='UTF-8') as f:
                data = json.load(f)
                for item in data:
                    if item["uniq_id"] == id:
                        data.remove(item)
                        with open(self.file_path, 'w', encoding='UTF-8') as f:
                            json.dump(data, f, indent=4)
                        return
        except FileNotFoundError:
            pass
"""
"""
    def update(self, entity, id):

        Method used to update data(entity) from a JSON file

        try:
            with open(self.file_path, 'r', encoding='UTF-8') as f:
                data = json.load(f)
            for item in data:
                if item["uniq_id"] == id:
                    data.remove(item)
                    entity["updated_at"] = datetime.datetime.now().isoformat()
                    data.append(entity)
                    with open(self.file_path, 'w', encoding='UTF-8') as f:
                        json.dump(data, f, indent=4)
                    return
        except FileNotFoundError:
            pass
"""
