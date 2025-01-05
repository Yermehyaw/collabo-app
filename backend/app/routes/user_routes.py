"""
Routes for user endpoints

MODULES:
    - fastapi: APIRouter, Depends, HTTPException
    - fastapi.security: OAuth2PasswordBearer
    - services.user_service: UserService
    - models.user: User, UserResponse
    - utils.auth.jwt_handler: verify_access_token

FUTURE IMPROVEMENTS:
    - utils.auth.jwt_handler: get_current_user
    - utils.auth.jwt_handler: get_current_active_user
    - utils.auth.jwt_handler: get_current_active_superuser

"""
from fastapi import (
    APIRouter, Depends,
    HTTPException
)
from fastapi.security import OAuth2PasswordBearer
from services.user_services import UserServices
from models.users import (
    UserUpdate, UserResponse
)
from utils.auth.jwt_handler import verify_access_token


user_router = APIRouter()
user_services = UserServices()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@user_router.get("/profile/{user_id}", response_model=UserResponse)
async def get_user_profile(user_id: str, token: str = Depends(oauth2_scheme)):
    """
    Route to get a user profile

    PARAMETERS:
        - user_id: str, user id
        - token: str, access token

    RETURNS:
        - UserResponse: user object

    """
    payload = verify_access_token(token)
    if not payload:
        failure = {"error": "Invalid token", "code": "UNAUTHORIZED"}
        raise HTTPException(status_code=401, detail=failure)

    user = await user_services.get_user_by_id(user_id)  # Returns a UserResponse obj
    if not user:
        failure = {"error": "User not found", "code": "NOT_FOUND"}
        raise HTTPException(status_code=404, detail=failure)

    return user


@user_router.put("/profile/{user_id}", response_model=dict)
async def update_user_profile(user_id: str, user: UserUpdate, token: str = Depends(oauth2_scheme)):
    """
    Route to update a user profile

    PARAMETERS:
        - user_id: str, user id
        - user: UserUpdate, json object with fields to be updated
        - token: str, access token

    RETURNS:
        - dict: update message

    NOTE:
    There is a "bug" in this implementation 🙃, the db storing users gets updated inspite no new data was passed innthe request.
    For example, a user could pass the same data twice or even the original data stored in the user and still get a update successful message. 
    So . . . .  🌚 whomever is readjng this, Its yr turn to ensyre that only requests with a change in data gets processsed or a diff message is sent like, "No data entries updated". Be of good faith soldier  😂❤️

    """
    token = verify_access_token(token)  # Decoded token
    if not token:
        failure = {"error": "Invalid token", "code": "UNAUTHORIZED"}
        raise HTTPException(status_code=401, detail=failure)
    
    if str(token["sub"]) != user_id:
        failure = {"error": "Permission denied", "code": "PERMISSION_DENIED"}
        raise HTTPException(status_code=403, detail=failure)

    fields_updated = await user_services.update_user(user_id, user)

    if fields_updated is None:  # user_id not found
        failure = {"error": "User not found", "code": "NOT_FOUND"}
        raise HTTPException(status_code=400, detail=failure)

    success = {"message": "profile updated successfully"}
    return success
