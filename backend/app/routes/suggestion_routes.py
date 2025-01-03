"""
Suggestions routes for user feed generation

MODULES:
    - fastapi: APIRouter, Depends, HTTPException, status
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
from typing import List
from services.suggestion_services import SuggestionServices
from app.models.projects import ProjectResponse
from app.models.users import UserResponse
from utils.auth.jwt_handler import verify_access_token

suggestion_router = APIRouter()
suggestion_services = SuggestionServices()

@suggestion_router.get("/projects/", response_model=List[ProjectResponse])
async def get_project_feed(token: str = Depends(verify_access_token)):
    """
    Route to get project suggestions for a user

    PARAMETERS:
        - token: str, access token

    RETURNS:
        - List[ProjectResponse]: json list of project objects
    """
    user_id = token.get("sub")
    return await suggestion_services.get_project_suggestions(user_id)

@suggestion_router.get("/users/", response_model=List[UserResponse])
async def get_user_feed(token: str = Depends(verify_access_token)):
    """
    Route to get user suggestions/recommendations for a collaboration

    PARAMETERS:
        - token: str, access token

    RETURNS:
        - List[UserResponse]: json list of user objects
    """
    user_id = token.get("sub")
    return await suggestion_services.get_user_suggestions(user_id)
