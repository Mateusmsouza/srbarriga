from os import getenv

from data.database import Mongo

def get_extract():
    database_connection = Mongo(getenv("MONGO_URI"))

    database_connection.