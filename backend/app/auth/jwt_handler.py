"""
JWT Handler module

MODULES:
    - jwt
    - datetime: datetime class
    - dotenv: load_dotenv function, load env variables
    - os: getenv function

"""
import jwt
from datetime import (
    datetime,
    timedelta
) 
from dotenv import load_dotenv
import os

load_dotenv()

JWT_SECRET = os.getenv("JWT_SECRET")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")
EXPIRES = 180  # Each user token expires in 3 hours


def create_access_token(data: dict):
    """
    Create a jwt access token

    ARGUMENTS:
        - data: dict, user data

    RETURNS:
        - token: str, jwt token

    """
    data_to_encode = data.copy()  # make a copy of the json dict
    expire = datetime.utcnow() + timedelta(minutes=EXPIRES)  # set the token expiration time

    data_to_encode.update({"exp": expire})  # add the expiration time to the data

    token = jwt.encode(data_to_encode, JWT_SECRET, algorithm=JWT_ALGORITHM)  # encode the data with the secret and the hashing algorithm
    return token


def verify_access_token(token: str):
    """
    Verify the jwt access token

    """
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])  # decode the token
        return payload
    except jwt.ExpiredSignatureError:
        return
    except jwt.InvalidTokenError:
        return
    except jwt.InvalidSubjectError:  # if the subject the token reprs is invalid
        return