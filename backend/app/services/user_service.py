"""
User Service Module
Handles all the business logic for the user model

MODULES:
    - typing: List, Optional, Union
    - datetime: datetime class
    - models.user: User
    - utils.auth.password_utils: hash_password, verify_password
    - utils.auth.jwt_handler: create_access_token, verify_access_token
    - db: get_collection, get collections from db client

"""
from typing import (
    List,
    Optional,
    Union
)
from datetime import datetime
from models.user import User
from utils.auth.password_utils import hash_password, verify_password
from utils.auth.jwt_handler import create_access_token, verify_access_token
from db import get_collection


class UserService:
    """
    User Services Class: Includes methods to create, authenticate, update, delete users and retrieve user data

    ATTRIBUTES:
        - collection_name: name of collection where user data in stored in the database   

    """

    def __init__(self):
        self.collection_name = "users"

    async def create_user(self, user: User.UserSignup) -> User:
        """
        Method to create a new user

        PARAMETERS:
            - user: User, user object

        RETURNS:
            - User: user object

        """
        # connect to collection
        collection = await get_collection(self.collection_name)

        existing_user = await self.get_user_by_email(user.email)
        if existing_user:
            raise ValueError("User already exists")
        
        user.password = hash_password(user.password)
        user.created_at = datetime.now()
        user.updated_at = datetime.now()

        # user.id = str(self.collection.insert_one(user.dict()).inserted_id)
        return user

    async def authenticate_user(self, email: str, password: str) -> Optional[User]:
        """
        Method to authenticate a user

        PARAMETERS:
            - email: str, email of the user
            - password: str, password of the user

        RETURNS:
            - User: user object

        """
        user = await self.get_user_by_email(email)
        if not user:
            return None
        if not verify_password(password, user.password):
            return None
        return user

    async def get_user_by_email(self, email: str) -> Optional[User]:
        """
        Method to get a user by email

        PARAMETERS:
            - email: str, email of the user

        RETURNS:
            - User: user object

        """
        user = await self.collection.find_one({"email": email})
        if user:
            return User(**user)
        return None

    async def get_user_by_id(self, user_id: str) -> Optional[User]:
        """
        Method to get a user by id

        PARAMETERS:
            - user_id: str, id of the user

        RETURNS:
            - User: user object

        """
        user = await self.collection.find_one({"id": user_id})
        if user:
            return User(**user)
        return None

    async def update_user(self, user_id: str, user: User) -> Optional[User]:
        """
        Method to update a user

        PARAMETERS:
            - user_id: str, id of the user
            - user: User, user object

        RETURNS:
            - User: user object

        """
        user.updated_at = datetime.now()
        updated_user = await self.collection.find_one_and_update(
            {"id": user_id},
            {"$set": user.dict()},
            return_document=True
        )
        if updated_user:
            return User(**updated_user)