from services.create_debt import create_debt
from services.get_extract import get_extract
from connections.send_message import send_message

if __name__ == "__main__":
    #create_debt()
    message = get_extract()
    print(message)
    #send_message(message=message)