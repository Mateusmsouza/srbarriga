import pymongo

class Mongo:

    def __init__(self, connection_string: str) -> None:
        self.client = pymongo.MongoClient(
            connection_string
        )

    def get_group(self):
        return self.client.group.people.find()

    def create_transaction(self, transaction):
        self.client.group.extract.insert_one(transaction)