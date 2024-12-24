"""
Searching endpoints

MODULES:
   - fastapi: APIRouter, Depends, HTTPException, status
   - typing: List
   - models.project: ProjectResponse
   - models.user: UserResponse
   - services.project_service: ProjectService
   - services.user_service: UserService 
   - utils.auth.jwt_handler: verify_access_token

"""
from fastapi import (
    APIRouter, Depends, Query,
    HTTPException, status
)
from typing import (
    Annotated, List, Union
)
from models.user import UserResponse
from models.project import ProjectResponse
from services.project_service import ProjectService
from services.user_service import UserService
from utils.auth.jwt_handler import verify_access_token

search_router = APIRouter()
project_service = ProjectService()
user_service = UserService()


@search_router.get("/users/", response_model=List[UserResponse])
async def search_users(
    token: str = Depends(verify_access_token), 
    name: Annotated[str, Query()] = None,
    skills: Annotated[Union[List[str], str, None], Query()] = [],  # can either be passed as a list, commas sep strings or a single string, yet is optional witha default of []
    interests: Annotated[Union[List[str], str, None], Query()] = [],
    projects: Annotated[Union[List[str], str, None], Query()] = [],
    followers: Annotated[Union[List[str], str, None], Query()] = [],
    following: Annotated[Union[List[str], str, None], Query()] = [],
    location: Annotated[str, Query()] = None,
):
    """
    Route to search for users

    PARAMETERS:
        - token: str, access token
        QUERY PARAMETERS:
            - q: str, search query

    RETURNS:
        - List[UserResponse]: list of user objects

    """
    query = {
        "name": name,
         "skills": skills,
         "interests": interests,
         "projects": projects,
         "followers": followers,
         "following": following,
         "location": location
   }
    users = await user_service.search_users(query)
    return users