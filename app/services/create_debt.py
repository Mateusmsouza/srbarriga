from os import getenv
from typing import Dict, List

from data.database import Mongo
from parser.transaction import parse_transaction
from services.users import get_users


def create_debt():
    database_connection = Mongo(getenv("MONGO_URI"))
    spotify_value = float(getenv("SPOTIFY_VALUE", 34.90))

    users = get_users(database_connection)
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
