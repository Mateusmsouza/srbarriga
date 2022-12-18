from os import getenv
from typing import Dict, List

from data.database import Mongo
from parser.transaction import parse_transaction
from services.users import get_users


def create_debt(user: str, value: float, description):
    database_connection = Mongo(getenv("MONGO_URI"))

    users = get_users(database_connection)
    
    transaction = database_connection.create_transaction(
        parse_transaction(
            value=spotify_value_by_user,
            type="DEBT",
            description="Monthly charge by automation",
            user=user["name"],
            user_id=user["id"],
        )
    )
