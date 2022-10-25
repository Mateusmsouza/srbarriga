from datetime import datetime

def parse_transaction(type: str, value: float, description: str, user: str, user_id: str):
    return {
        "type": type,
        "value": value,
        "details": {
            "description": description,
            "user": user,
            "user_id": user_id,
            "created_at": datetime.today().strftime('%Y-%m-%d')
        }
    }
