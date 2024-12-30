"""
Friends models for connecting users as friends
Comprises the FriendRequestModel, FriendResponseModel, and FriendshipResponse models

MODULES:
    - pydantic: BaseModel
    - typing: List, Optional
    - datetime: datetime class

"""
from pydantic import BaseModel
from typing import (
    List, Optional
)
from datetime import datetime


class FriendRequestCreate(BaseModel):
    """
    Model to send a friend request to a user

    ATTRIBUTES:
         - recipient_id: str, id of the user the request is sent to

    """
    recipient_id: str


class FriendRequestResponse(BaseModel):
    """
    Model to respond and retrieve a friend request obj

    ATTRIBUTES:
        - id: id, unique id of a request
        - sender_id: str, id of the user who sent the request
        - recipient_id: str, id of the receipient
        - status: literal str, status of the request i.e pending, accepted or refused
        - created_at: str, datetime when the request was sent/created

    """
    id: str
    sender_id: str
    recipient_id: str
    status: Literal["pending", "accepted", "refused"] = "pending"
    created_at: str = datetime.now().isoformat()


class FriendshipResponse(BaseModel):
    """
    Model to define and display a friendship relationship between users

    ATTRIBUTED:
         - user_id: str, id of the user in the friendship
         - name: str, name of friend
         - created_at: str, datetime
    """
    user_id: str
    name: Optional[str]
    created_at: str
