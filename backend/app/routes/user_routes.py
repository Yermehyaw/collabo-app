"""
Routes for user endpoints

MODULES:
    - fastapi: APIRouter, Depends, HTTPException, status
    - services.user_service: UserService
    - models.user: User, UserResponse
    - utils.auth.password_utils: verify_password
    - utils.auth.jwt_handler: verify_access_token

FUTURE IMPROVEMENTS:
    - utils.auth.jwt_handler: get_current_user
    - utils.auth.jwt_handler: get_current_active_user
    - utils.auth.jwt_handler: get_current_active_superuser

"""
from fastapi import APIRouter, Depends, HTTPException, status
from typing_extensions import Annotated
from services.user_service import UserService
from models.user import User, UserResponse
from utils.auth.password_utils import verify_password
from utils.auth.jwt_handler import verify_access_token

user_router = APIRouter()
user_service = UserService()

@user_router.get("/profile/{user_id}", response_model=UserResponse)
async def get_user_profile(user_id: str, token: str = Depends(verify_access_token)):
    """
    Route to get a user profile

    PARAMETERS:
        - user_id: str, user id
        - token: str, access token

    RETURNS:
        - UserResponse: user object

    """
    user = await user_service.get_user_by_id(user_id)
    if not user:
        failure = {}
        raise HTTPException(status_code=404, detail=failure)
    
    user_resp = UserResponse()
    user_resp = {key: user[key] for key in user if key in user_resp}  # copy all mutual key-value pairs from user obj to userResp obj
    return user_resp

@user_router.put("/profile/{user_id}", response_model=UserResponse)
async def update_user_profile(user_id: str, user: User, token: str = Depends(verify_access_token)):
    """
    Route to update a user profile

    PARAMETERS:
        - user_id: str, user id
        - user: User, user object
        - token: str, access token

    RETURNS:
        - UserResponse: updated user object

    """
    if user_id != user.user_id:
        raise HTTPException(status_code=400, detail="User id does not match")
    updated_user = await user_service.update_user(user)
    return updated_user
