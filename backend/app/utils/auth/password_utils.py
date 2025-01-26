"""
Password management utilities/module

MODULES:
    - bcrypt: checkpw, gensalt, hashpw functions

"""
from bcrypt import (
    checkpw,
    gensalt,
    hashpw
)


def hash_password(password: str) -> str:
    """
    Hash the password

    ARGUMENTS:
        - password: str, user password

    RETURNS:
        - hashed_password: str, hashed password

    """
    return hashpw(password.encode("utf-8"), gensalt()).decode("utf-8")


def verify_password(password: str, hashed_password: str) -> bool:
    """
    Check if the password matches the hashed password

    ARGUMENTS:
        - password: str, user password
        - hashed_password: str, hashed password

    RETURNS:
        - bool, True if the password matches the hashed password, False otherwise

    """
    return checkpw(password.encode("utf-8"), hashed_password.encode("utf-8"))
