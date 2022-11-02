from os import getenv
from typing import Dict, List
from datetime import datetime


from data.database import Mongo
from services.users import get_users

def get_extract():
    database_connection = Mongo(getenv("MONGO_URI"))
    transactions = database_connection.get_transactions()
    message =  f"Reporte do Sr Barriga de {datetime.today().strftime('%Y-%m-%d')}\n\n"
    users = get_users(database_connection)
    users_and_bill = {}

    for user in users:
        users_and_bill[user["name"]] = {
            "DEBT": [],
            "CREDIT": []
        }

    for transaction in transactions:
        transaction_type = transaction["type"]
        transaction_user = transaction["details"]["user"]
        if  transaction_type == "DEBT" and transaction_user in [user["name"] for user in users]:
            users_and_bill[transaction_user]["DEBT"].append(transaction["value"])
        elif transaction_type == "CREDIT" and transaction_user in [user["name"] for user in users]:
            users_and_bill[transaction_user]["CREDIT"].append(transaction["value"])

    for user, extracts in users_and_bill.items():
        sum_by_user = sum(extracts['CREDIT']) - sum(extracts['DEBT'])
        message += f"O saldo atual do (a) {user} é R$ {round(sum_by_user, 2)}\n"

    return message