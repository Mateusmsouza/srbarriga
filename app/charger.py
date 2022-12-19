from os import getenv

from services.create_debt import create_debt
from services.get_extract import get_extract
from connections.send_message import send_message

if __name__ == "__main__":
    create_debt()
    message = get_extract()
    call_send_message = int(getenv("SEND_NOTIFICATION", 1))
    if call_send_message:
        send_message(message=message)
