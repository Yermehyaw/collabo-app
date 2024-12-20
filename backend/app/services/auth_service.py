"""
Auth Service Module
Handles all the business logic for authenticating users

MODULES:
    - typing: List, Optional, Union
    - datetime: datetime class
    - models.user: User
    - utils.auth.password_utils: hash_password, verify_password
    - utils.auth.jwt_handler: create_access_token
    - db: get_collection, get collections from db client
    - pydantic: ValidationError
    - bson: ObjectId

"""
from typing import (
    List,
    Optional,
    Union
)
from datetime import datetime
from models.user import (
    User, UserSignup, UserResponse, Token
)
from utils.auth.password_utils import hash_password, verify_password
from utils.auth.jwt_handler import create_access_token
from db import get_collection
from pydantic import ValidationError
from bson import ObjectId


class AuthService:
    """
    Auth Services Class: Includes methods create/signup or login/authenticate users

    ATTRIBUTES:
        - collection_name: name of collection where user data in stored in the database   

    """

    def __init__(self):
        self.collection_name = "users"

    async def create_user(self, signup: UserSignup) -> str:
        """
        Method to create a new user

        PARAMETERS:
            - user: User, user object

        RETURNS:
            - user_id: id of newly created and stored user object

        """
        # connect to collection
        collection = await get_collection(self.collection_name)

        existing_user = await self.get_user_by_email(signup.email)
        if existing_user:
            raise ValueError("User already exists")

        p_hash = hash_password(signup.password)
        user = User(name=signup.name, email=signup.email, password=p_hash)

        insertion_id = collection.insert_one(
            user.model_dump(by_alias=True)).inserted_id  # user obj must be transformed into a dict using model_dump() or dict()

        return str(insertion_id)  # same as the user_id because alias of user_id which is _id was set to True

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
        if not verify_password(password, user.password):
            return None
        
        access_token = create_access_token(data={"sub": user.user_id, "email": user.email})
        token = Token(access_token=access_token, token_type="bearer")
        return token

    async def get_user_by_email(self, email: str) -> Optional[UserResponse]:
        """
        Method to get a user by email

        PARAMETERS:
            - email: str, email of the user

        RETURNS:
            - User: user object

        """
        collection = await get_collection(self.collection_name)
        user = await collection.find_one({"email": email}, {"pasword": 0})  # get by email but exclude password field from output
        if user:
            return UserResponse(**user)
        return None
