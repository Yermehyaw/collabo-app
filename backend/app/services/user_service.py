"""
User Service Module
Handles all the business logic for the user model

MODULES:
    - typing: List, Optional, Union
    - datetime: datetime class
    - models.user: User
    - db: get_collection, get collections from db client

"""
from typing import (
    List,
    Optional,
    Union
)
from datetime import datetime
from models.user import User
from db import get_collection


class UserService:
    """
    User Services Class: Includes methods to update, delete users and retrieve user data

    ATTRIBUTES:
        - collection_name: name of collection where user data in stored in the database   

    """

    def __init__(self):
        self.collection_name = "users"


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
            - user_id: str, id of the user

        RETURNS:
            - User: user object

        """
        collection = await get_collection(self.collection_name)
        user = await collection.find_one({"user_id": user_id})
        if user:
            return User(**user)
        return None

    async def update_user(self, _id: str, user: User) -> Optional[User]:
        """
        Method to update a user

        PARAMETERS:
            - _id: str, db id of the user doc
            - user: User, sample user object to be used to update the user in the database

        RETURNS:
            - User: user object

        """
        collection = await get_collection(self.collection_name)
        user.updated_at = datetime.now().isoformat()
        
        updated_user = await collection.find_one_and_update(
            {"db_id": _id},
            {"$set": user.dict()},
            return_document=True
        )
        if updated_user:
            return User(**updated_user)
