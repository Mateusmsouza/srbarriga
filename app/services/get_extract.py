from os import getenv
from typing import Dict, List

from data.database import Mongo

def get_extract(users: List[Dict]):
    database_connection = Mongo(getenv("MONGO_URI"))
    transactions = database_connection.get_transactions()

    users_and_bill = {}

    for user in users:
        users_and_bill[user["name"]] = {
            "DEBT": [],
            "CREDIT": []
        }
    print(users)
    for transaction in transactions:
        print(transaction)
        transaction_type = transaction["type"]
        transaction_user = transaction["details"]["user"]

        if  transaction_type == "DEBT" and transaction_user in [user["name"] for user in users]:
            print("DEBT")
            users_and_bill[transaction_user]["DEBT"].append(transaction["value"])
        elif transaction_type == "CREDIT" and transaction_user in users:
            print("CREDIT")
            users_and_bill[transaction_user]["CREDIT"].append(transaction["value"])

    for user, extracts in users_and_bill.items():
        sum_by_user = sum(extracts['CREDIT']) - sum(extracts['DEBT'])
        print(f"O saldo atual do (a) {user} é R$ {round(sum_by_user, 2)}")