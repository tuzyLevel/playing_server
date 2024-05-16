from encryption import get_hashed_password


def validate_password(input_password: str, salt: str, hashed_password: str):
    if (get_hashed_password(input_password, salt) == hashed_password):
        return True
    else:
        return False
