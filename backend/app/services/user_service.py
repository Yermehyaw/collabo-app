"""
User Service Module
Handles all the business logic for the user model

MODULES:
    - datetime: datetime class
    - models.user: UserUpdate, UserResponse
    - db: get_collection, get collections from db client
    - bson: ObjectId, validate and create byte ids

"""
from typing import Optional
from datetime import datetime
from models.user import (
    UserUpdate, UserResponse
)
from db import get_collection
from bson import ObjectId


class UserService:
    """
    User Services Class: Includes methods to update, delete users and retrieve user data

    ATTRIBUTES:
        - collection_name: name of collection where user data in stored in the database   

    """

    def __init__(self):
        self.collection_name = "users"

    async def get_user_by_id(self, user_id: str) -> Optional[UserResponse]:
        """
        Method to get a user by id

        PARAMETERS:
            - user_id: str, unique id of the user

        RETURNS:
            - User: user object

        """
        collection = await get_collection(self.collection_name)

        if not ObjectId.is_valid(user_id):  # validate that the id is first a valid objectid. ObjectId is the type used by mongodb to assign ids to its entries
            return None

        user = await collection.find_one({"_id": ObjectId(user_id)}, {"password": 0})
        if user:
            return UserResponse(**user)
        return None

    async def update_user(self, user_id: str, user: UserUpdate) -> Optional[int]:
        """
        Method to update a user

        PARAMETERS:
            - user_id: str, db id of the user doc
            - user: User, sample user object to be used to update the user in the database

        RETURNS:
            - int: no of fields updated

        """
        collection = await get_collection(self.collection_name)

        if not ObjectId.is_valid(user_id):
            return None

        user.updated_at = datetime.now().isoformat()
        update_response = await collection.update_one(
            {"_id": ObjectId(user_id)},
            {"$set": user.model_dump()},
        )  # update_one never returns none even if no document was flund with the user_id

        if not update_response.matched_count:
            return None # document with user_id dosent exist

        return update_response.modified_count
