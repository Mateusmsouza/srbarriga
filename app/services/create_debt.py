from os import getenv
from typing import Dict, List

from data.database import Mongo
from parser.transaction import parse_transaction


def create_debt():
    database_connection = Mongo(getenv("MONGO_URI"))
    spotify_value = float(getenv("SPOTIFY_VALUE", 34.90))

    users = __get_users(database_connection)
    transactions = []
    spotify_value_by_user = round(spotify_value/(len(users) + 1), 2)
    for user in users:
        transaction = database_connection.create_transaction(
            parse_transaction(
                value=spotify_value_by_user,
                type="DEBT",
                description="Monthly charge by automation",
                user=user["name"],
                user_id=user["id"]
            ))
        transactions.append(transaction)

    return users, transactions

def __get_users(database: Mongo) -> List[Dict]:
    users = []
    for user in database.get_group():
        users.append({
            "id": str(user["_id"]),
            "name": user["name"]
        })
    
    return users