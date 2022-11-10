from data.database import Mongo
from typing import Dict, List


def get_users(database: Mongo) -> List[Dict]:
    users = []
    for user in database.get_group():
        users.append({"id": str(user["_id"]), "name": user["name"]})

    return users
