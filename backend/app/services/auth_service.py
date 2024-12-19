"""
Auth Service Module
Handles all the business logic for authenticating users

MODULES:
    - typing: List, Optional, Union
    - datetime: datetime class
    - models.user: User
    - utils.auth.password_utils: hash_password, verify_password
    - db: get_collection, get collections from db client

"""
from typing import (
    List,
    Optional,
    Union
)
from datetime import datetime
from models.user import User, UserSignup
from utils.auth.password_utils import hash_password, verify_password
from db import get_collection


class AuthService:
    """
    Auth Services Class: Includes methods create/signup or login/authenticate users

    ATTRIBUTES:
        - collection_name: name of collection where user data in stored in the database   

    """

    def __init__(self):
        self.collection_name = "users"

    async def create_user(self, signup: UserSignup) -> User:
        """
        Method to create a new user

        PARAMETERS:
            - user: User, user object

        RETURNS:
            - User: newly created and stored user object

        """
        # connect to collection
        collection = await get_collection(self.collection_name)

        existing_user = await self.get_user_by_email(signup.email)
        if existing_user:
            raise ValueError("User already exists")
        
        user = User()
        user.password = hash_password(signup.password)
        db_id = str(collection.insert_one(user.dict()).inserted_id)  # insert user into collection and store the  id as an attr of the user obj
        user.db_id = db_id
        
        return user

    async def authenticate_user(self, email: str, password: str) -> Optional[User]:
        """
        Method to authenticate/login a user. Generates a unique access token for the user

        PARAMETERS:
            - email: str, email of the user
            - password: str, password of the user

        RETURNS:
            - user: authenticated user object

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
        collection = await get_collection(self.collection_name)
        user = await collection.find_one({"email": email})
        if user:
            return User(**user)  # the dict returned from is unpacked and turned into a User object
        return None

    async def get_user_by_id(self, user_id: str) -> Optional[User]:
        """
        Method to get a user by id

        PARAMETERS:
            - user_id: str, unique id of the user

        RETURNS:
            - User: user object

        """
        collection = await get_collection(self.collection_name)
        user = await collection.find_one({"user_id": user_id})
        if user:
            return User(**user)
        return None
