import argparse
from os import getenv
from services.create_payment import create_payment
from connections.send_message import send_message

parser = argparse.ArgumentParser(
    prog="Sr Barriga Payment Workflow",
    description="Execute payment Workflow"
)

parser.add_argument(
    "-u", "--user", "--user to create a payment", type=str)

parser.add_argument(
    "-v", "--value", "--value to create a payment", type=float)

parser.add_argument(
    "-d", "--description", "--payment description", type=str)

if __name__ == "__main__":
    args = parser.parse_args()
    create_payment(
        args.user,
        args.value,
        args.description)
    
    call_send_message = int(getenv('SEND_NOTIFICATION', 1))
    if call_send_message:
        message =  f"Pagamento de {args.user} (R$ {args.value}) realizado :)"
        send_message(message=message)
