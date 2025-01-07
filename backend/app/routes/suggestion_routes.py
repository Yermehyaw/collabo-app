"""
Suggestions routes for user feed generation

MODULES:
    - fastapi: APIRouter, Depends, HTTPException, status
    - fastapi.security: OAuth2PasswordBearer
    - typing: List
    - services.suggestion_services: SuggestionServices
    - models.projects: ProjectResponse
    - models.user: UserResponse
    - utils.auth.jwt_handler: verify_access_token

"""
from fastapi import (
    APIRouter, Depends,
    status, HTTPException
)
from fastapi.security import OAuth2PasswordBearer
from typing import List
from services.suggestion_services import SuggestionServices
from models.projects import ProjectResponse
from models.users import UserResponse
from utils.auth.jwt_handler import verify_access_token

suggestion_router = APIRouter()
suggestion_services = SuggestionServices()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@suggestion_router.get("/projects/", response_model=List[ProjectResponse])
async def get_project_feed(token: str = Depends(oauth2_scheme)):
    """
    Route to get project suggestions for a user

    PARAMETERS:
        - token: str, access token

    RETURNS:
        - List[ProjectResponse]: json list of project objects
    """
    token = verify_access_token(token)
    if not token:
        failure = {"error": "Invalid token", "code": "UNAUTHORIZED"}
        raise HTTPException(status_code=401, detail=failure)
    
    user_id = token.get("sub")
    return await suggestion_services.get_project_suggestions(user_id)


@suggestion_router.get("/users/", response_model=List[UserResponse])
async def get_user_feed(token: str = Depends(oauth2_scheme)):
    """
    Route to get user suggestions/recommendations for a collaboration

    PARAMETERS:
        - token: str, access token

    RETURNS:
        - List[UserResponse]: json list of user objects
    """
    token = verify_access_token(token)
    if not token:
        failure = {"error": "Invalid token", "code": "UNAUTHORIZED"}
        raise HTTPException(status_code=401, detail=failure)

    user_id = token.get("sub")
    return await suggestion_services.get_user_suggestions(user_id)
