from os import getenv
from typing import Dict, List

from data.database import Mongo


def create_debt():
    database_connection = Mongo(getenv("MONGO_URI"))
    spotify_value = getenv("SPOTIFY_VALUE", 34,90)

    users = __get_users(database_connection)

    for user in users:
        database_connection.create_transaction(

        )

def __get_users(database: Mongo) -> List[Dict]:
    users = []
    for user in database.get_group():
        users.append({
            "id": str(user["_id"]),
            "name": user["name"]
        })
    
    return users