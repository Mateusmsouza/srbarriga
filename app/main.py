from services.create_debt import create_debt
from services.get_extract import get_extract

if __name__ == "__main__":
    users, _ = create_debt()
    get_extract(users)