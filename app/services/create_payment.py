from os import getenv

from data.database import Mongo
from parser.transaction import parse_transaction
from services.users import get_user_by_name


def create_payment(name: str, value: float, description):
    database_connection = Mongo(getenv("MONGO_URI"))

    user = get_user_by_name(database_connection, name)
    database_connection.create_transaction(
        parse_transaction(
            value=value,
            type="CREDIT",
            description=f"CI Payment Workflow: {description}",
            user=user["name"],
            user_id=str(user["_id"]),
        )
    )
