"""
Routes for user endpoints

MODULES:
    - fastapi: APIRouter, Depends, HTTPException
    - services.user_service: UserService
    - models.user: User, UserResponse
    - utils.auth.password_utils: verify_password
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
from backend.app.services.user_services import UserService
from backend.app.models.users import (
    UserUpdate, UserResponse
)
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
        failure = {"error": "User not found", "code": "NOT_FOUND"}
        raise HTTPException(status_code=404, detail=failure)

    return user


@user_router.put("/profile/{user_id}", response_model=UserResponse)
async def update_user_profile(user_id: str, user: UserUpdate, token: str = Depends(verify_access_token)):
    """
    Route to update a user profile

    PARAMETERS:
        - user_id: str, user id
        - token: str, access token

    RETURNS:
        - UserResponse: updated user object

    """
    if str(token["sub"]) != user_id:
        failure = {"error": "Permission denied", "code": "PERMISSION_DENIED"}
        raise HTTPException(status_code=403, detail=failure)

    fields_updated = await user_service.update_user(user_id, user)

    if fields_updated is None:  # user_id not found
        failure = {"error": "User not found", "code": "NOT_FOUND"}
        raise HTTPException(status_code=400, detail=failure)

    if fields_updated == 0:  # user_id found, but no change
        success = {"message": "No data entries updated/created"}
    else:
        success = {"message": "profile updated successfully"}

    return success
