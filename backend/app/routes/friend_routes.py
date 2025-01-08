"""
Friends Routes
Routes to handle sending and receiving friend requests and getting the list of friends of a user

MODULES:
   - fastapi: APIRouter, Depends, HTTPException, status
   - fastapi.security: OAuthPasswordBearer
   - typing: Literal, List
   - services.friend_services: FriendServices
   - models.friends: FriendRequestCreate, FriendshipResponse
   - utils.auth.jwt_handler: verify_access_token

"""
from fastapi import (
    APIRouter, Depends,
    HTTPException, status
)
from fastapi.security import OAuthPasswordBearer
from typing import (
    Literal, List
)
from services.friend_services import FriendServices
from services.user_services import UserServices
from models.friends import (
    FriendRequestCreate, FriendshipResponse
)
from utils.auth.jwt_handler import verify_access_token


friend_router = APIRouter()
user_services = UserServices()
friend_services = FriendServices()
oauth2_scheme = OAuthPasswordBearer(tokenUrl="token")


@friend_services.post("/requests", response_model=dict, status_code=status.HTTP_201_CREATED)
async def send_request(request: FriendRequestCreate, token: str = Depends(oauth2_scheme)):
    """
    Send a request to a user

    PARAMETERS:
       - request: FriendRequestCreate, holds the recipient id
       - token: str, auth token

    RETURNS:
       - message: JSON dict, response message or error

    """
    token = verify_access_token(token)  # Decoded token
    if not token:
        failure = {"error": "Invalid token", "code": "UNAUTHORIZED"}
        raise HTTPException(status_code=401, detail=failure)
    
    user_id = token.get("sub")
    request_id = await friend_services.send_friend_request(user_id, request.recipient_id)

    if not request_id:
        failure = {"error": "Request exists already", "code": "BAD_REQUEST"}
        raise HTTPException(status_code=400, detail=failure)

    success = {"message": "Request sent successfully", "request_id": request_id}
    return success


@friend_router.put("/requests/{request_id}", response_model=dict)
async def respond_to_request(request_id: str, status: Literal["accepted", "rejected"], token: str = Depends(oauth2_scheme)):
    """
    Respond to a friend request

    PARAMETRS:
       - request_id: str, id of request
       - status: str, new status of request. Can either be "accepted" or "rejected"

    RETURNS:
       - message: JSON dict, response message or error

    """
    token = verify_access_token(token)  # Decoded token
    if not token:
        failure = {"error": "Invalid token", "code": "UNAUTHORIZED"}
        raise HTTPException(status_code=401, detail=failure)

    # Validate the update request was sent by one to whom the request was sent
    user_id = token.get("sub")
    result = await friend_services.get_request_by_id(request_id)
    if not result or result.recipient_id != user_id:
        failure = {"error": "You are not permitted to update this request", "code": "PERMISSION_DENIED"}  # To improve security, this should be obfuscated as a 404 err
        raise HTTPException(status_code=403, detail=failure)

    updated_response = await friend_services.update_friend_request_status(request_id, status)
    if not updated_response:
        failure = {"error": "Request not found", "code": "NOT_FOUND"}
        raise HTTPException(status_code=404, detail=failure)

    success = {"message": f"Request status updated successfully: {status}"}
    return success


@friend_router.get("/", response_model=List[FriendshipResponse])
async def get_friends(token: str = Depends(oauth2_scheme)):
    """
    Retrieve the list of friends of a user

    ATTRIBUTES:
        - token: str, jwt auth token

    RETURNS:
        - list: list of friend objects
    """
    token = verify_access_token(token)  # Decoded token
    if not token:
        failure = {"error": "Invalid token", "code": "UNAUTHORIZED"}
        raise HTTPException(status_code=401, detail=failure)

    user_id = token.get("sub")
    friends = await friend_services.get_friend_list(user_id)  # returns both ids of the users in the friendship

    friends = [  # Im sorry . . . 
        {
            "user_id": friend["user1_id"] if friend["user2_id"] == user_id else friend["user2_id"],  # id shouldnt be the user_id, its the id of the second user in friendship with the user
            "name": await user_services.get_user_by_id(
                friend["user1_id"] if friend["user2_id"] == user_id else friend["user2_id"]
            ).name,   # get the nane of the second user
            "created_at": friend["created_at"]
         }
        for friend in friends  # This is a list comprehension
    ]

    return friends
