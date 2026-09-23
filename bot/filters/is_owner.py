from config import OWNER_ID


def is_owner(user_id: int) -> bool:
    return str(user_id) == str(OWNER_ID)
