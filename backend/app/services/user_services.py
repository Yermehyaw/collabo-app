"""
User Service Module
Handles all the business logic for the user model

MODULES:
    - datetime: datetime class
    - models.user: UserUpdate, UserResponse
    - db: get_collection, get collections from db client

"""
from typing import Optional
from datetime import datetime
from models.users import (
    UserUpdate, UserResponse
)
from db import get_collection


class UserServices:
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

        #if not ObjectId.is_valid(user_id):  # validate that the id is first a valid objectid. ObjectId is the type used by mongodb to assign ids to its entries
        #    return None

        user = await collection.find_one({"_id": user_id}, {"password": 0})
        if user:
            user["user_id"] = user.pop("_id")
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

        # if not ObjectId.is_valid(user_id):
        #    return None

        update_data = user.model_dump(exclude_unset=True)  # exclude fields which are None

        list_fields = {}
        other_fields = {}
        for key, value in update_data.items():
            if isinstance(key, list):
                list_fields.update({key: value})
            else:  # key is a string, int or any other type
                other_fields.update({key: value})

        # Update list and string values fields separately
        update_response = await collection.update_one(
            {"_id": user_id},
            {
                "$addToSet": list_fields,  # addToSet adds the value to the array field only if its not already present
                "$set": other_fields
            }
        )  # update_one never returns none even if no document was flund with the user_id
        
        if update_response.matched_count == 0:
            return None # document with user_id dosent exist

        return update_response.modified_count

    async def search_users(self, filters: dict) -> list:
        """
        Method to search for users

        PARAMETERS:
            - filters: dict, filter params to be used in the search

        RETURNS:
            - list: list of user objects

        """
        collection = await get_collection(self.collection_name)

        # Create custom query dict from the filters dict received
        if not filters:
            return []
        
        query = {}
        for key, value in filters.items():
            if key == "name":
                if value:
                    query[key] = {"$regex": value, "$options": "i"}
            
            if key == "skills":
                if isinstance(value, str):
                    query[key] = {"$in": value.split(", ")}
                else:
                    query[key] = {"$in": value}

            if key == "interests":
                if isinstance(value, str):
                    query[key] = {"$in": value.split(", ")}
                else:
                    query[key] = {"$in": value}
            
            if key == "location":
                if value:  # Location is non-null
                    query[key] = {"$regex": value, "$options": "i"}
            
            if key == "language":
                if value:
                    query[key] = {"$regex": value, "$options": "i"}

            if key == "timezone":
                if value:
                    query[key] = {"$regex": value, "$options": "i"}

        users = await collection.find(query).to_list(length=None)

        for user in users:
            user.pop("password")
            user["user_id"] = user.pop("_id")

        return [UserResponse(**user) for user in users]

    async def submit_friend_request(self, receipient: str):
        """
        Submit a friendship/connect request to a user

        PARAMETERS:
            - receipient: str, user id of the receipient of the connect request

        """
        pass

    async def update_friend_request_status(self, sender: str, status: str):
        """
        Update the status of a friend request

        PARAMETERS:
            - sender: str, user id of the sender of the request
            - status: str, status of the request

        """
        pass
