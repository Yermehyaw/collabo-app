"""
Friend services
Handles logic to send, receive and response to friend requests

MODULES:
   - db: get_collection
   - bson: ObjectId
   - datetime: datetime class
   - models.friends: FriendRequestResponse, FriendshipResponse
   - services.user_services: UserServices

"""
from db import get_collection
from bson import ObjectId
from datetime import datetime
from models.friends import (
    FriendRequestResponse, FriendshipResponse
)
from services.user_services import UserServices


user_services = UserServices()


class FriendServices:
    """
    Comprises methods to send, receuve and update friend request status as well as get the friends list for a user

    ATTRIBUTES:
        - requests: name of friend requests collection
        - friendship: name of friendship relationship collection

    """
    def __init__(self):
        """Object initializer"""
        self.requests_collection = "friend_requests"
        self.friendship_collection = "friendships"

    async def send_friend_request(self, sender_id: str, recipient_id: str):
        """
        Send friend request to a user

        PARAMETERS:
           - sender_id: str, id of the sender
           - recipient_id: str, id if recipient
        
        RETURNS:
           - id: str, id of new request
        """
        collection = await get_collection(self.requests_collection)
        existing_request = await collection.find_one({"sender_id": sender_id, "recipient_id": recipient_id})
        if existing_request:
            return None  # Avoid sending multiple requests

        # Validate the receipoent exists
        user = await user_services.get_user_by_id(recipient_id)
        if not user:
            return None

        request = FriendRequestResponse(sender_id=sender_id, recipient_id=recipient_id)
        insertion = await collection.insert_one(request.model_dump())
        request_id = str(insertion.inserted_id)

        return request_id

    async def get_request_by_id(self, request_id: str):
        """
        Get friend request by id

        PARAMETERS:
           - request_id: str, id of the request

        RETURNS:
           - request: dict, format of FriendRequestResponse but with a _id attr

        """
        if not ObjectId.is_valid(request_id):
            return None

        collection = await get_collection(self.requests_collection)
        request = await collection.find_one({"_id": ObjectId(request_id)})

        return request


    async def update_friend_request_status(self, request_id: str, status: str ):
        """
        Updates the status of a friend request

        PARAMETERS:
            - request_id: str, id of a friend request
            - status: str, new status of the update

        RETURNS:
           - int: no of obj in db updated, expected = 1
        
        """
        request = self.get_request_by_id(request_id)
        if not request:  # id is valid but dosent match any request in the db
            return None  # 404 err
        
        if status == "accepted":  # create a friendship
            collection = await get_collection(self.friendship_collection)
            friendship = {
                "user1_id": request["sender_id"],
                "user2_id": request["recipient_id"],
                "created_at": datetime.now().isoformat()
            }
            await collection.insert_one(friendship)

        updated = await collection.update(
            {"_id": ObjectId(request_id)},
            {"$set": {"status": status}}
        )
        return updated.modified_count


    async def get_friend_list(self, user_id: str):
        """
        Get list of friends of a user

        PARAMETERS:
           - user_id: str, id of user

        RETURNS:
           - list: list of friendships(format of FriendshipResponse)

        """
        collection = await get_collection(self.friendship_collection)
        friends = await collection.find(
            {"$or": [{"user1_id": user_id}, {"user2_id": user_id}]}
        ).to_list()  # a length arg can be passed to to_list() for pagination
        return friends
