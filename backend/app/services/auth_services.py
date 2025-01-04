"""
Auth Services Module
Handles all the business logic for authenticating users

MODULES:
    - typing: List, Optional, Union
    - models.users: UserCreate
    - utils.auth.password_utils: hash_password, verify_password
    - utils.auth.jwt_handler: create_access_token
    - db: get_collection, get collections from db client
    - pydantic: ValidationError
    - uuid: uuid4 method

"""
from typing import (
    Optional,
)
from models.users import (
    UserCreate, UserSignup, UserResponse, Token
)
from utils.auth.password_utils import hash_password, verify_password
from utils.auth.jwt_handler import create_access_token
from db import get_collection
from pydantic import ValidationError
from uuid import uuid4


class AuthServices:
    """
    Auth Services Class: Includes methods create/signup or login/authenticate users

    ATTRIBUTES:
        - collection_name: name of collection where user data in stored in the database   

    """

    def __init__(self):
        self.collection_name = "users"

    async def create_user(self, signup: dict) -> str:
        """
        Method to create a new user

        PARAMETERS:
            - user: dict, with params to build a user object

        RETURNS:
            - user_id: id of newly created and stored user object

        """
        # connect to collection
        collection = await get_collection(self.collection_name)

        # Check if user already exists
        existing_user = await self.get_user_by_email(signup.email)
        if existing_user:
            raise ValueError("User already exists")

        # Building user obj for insertion into the DB
        p_hash = hash_password(signup.password)
        user = UserCreate(name=signup.name, email=signup.email, password=p_hash)
        
        user_data = user.model_dump(by_alias=True)  # user obj must first transformed into a simple dict, with the use of by_alias=True to use the alias name of user_id
        user_data["_id"] = 'user' + str(uuid4()) # optimise retrieval by setting user_id to the indexed _id
        
        
        insertion = await collection.insert_one(user_data)

        return str(insertion.inserted_id)  # new_id should now be the the same as insertion_id

    async def authenticate_user(self, email: str, password: str) -> Optional[Token]:
        """
        Method to authenticate/login a user. Generates a unique access token for the user

        PARAMETERS:
            - email: str, email of the user
            - password: str, password of the user

        RETURNS:
            - Token: token dict of the authenticated user

        """
        user = await self.get_user_by_email(email)
        if not user:
            return None
        if not verify_password(password, user["password"]):
            return None
        
        access_token = create_access_token(data={"sub": user["user_id"], "email": user["email"]})
        token = Token(access_token=access_token, token_type="bearer")
        return token

    async def get_user_by_email(self, email: str) -> Optional[dict]:
        """
        Method to get a user by email

        PARAMETERS:
            - email: str, email of the user

        RETURNS:
            - dict: dict of user object

        """
        collection = await get_collection(self.collection_name)
        user = await collection.find_one({"email": email})
        user["user_id"] = user.pop("_id")
        if user:
            return user
        return None
