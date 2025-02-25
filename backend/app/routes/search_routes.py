"""
Searching endpoints

MODULES:
   - fastapi: APIRouter, Depends, HTTPException, status
    - fastapi.security: OAuth2PasswordBearer
   - typing: List, Union
   - typing_extensions: Annotated
   - models.projects: ProjectResponse
   - models.users: UserResponse
   - services.project_service: ProjectService
   - services.user_service: UserService 
   - utils.auth.jwt_handler: verify_access_token

"""
from fastapi import (
    APIRouter, Depends, Query,
    HTTPException, status
)
from fastapi.security import OAuth2PasswordBearer
from typing import (
    List, Union
)
from typing_extensions import Annotated
from models.users import UserResponse
from models.projects import ProjectResponse
from services.project_services import ProjectServices
from services.user_services import UserServices
from utils.auth.jwt_handler import verify_access_token

search_router = APIRouter()
project_services = ProjectServices()
user_services = UserServices()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@search_router.get("/users/", response_model=List[UserResponse])
async def search_users(
    token: str = Depends(oauth2_scheme), 
    name: Annotated[Union[str, None], Query()] = None,
    location: Annotated[Union[str, None], Query()] = None,
    skills: Annotated[Union[List[str], str, None], Query()] = [],  # can either be passed as a list, commas sep strings or a single string, yet is optional witha default of []
    interests: Annotated[Union[List[str], str, None], Query()] = [],
    timezone: Annotated[Union[str, None], Query()] = None,
):
    """
    Route to search for users

    PARAMETERS:
        - token: str, access token
        QUERY PARAMETERS:
            - name: str, search query, name of the user
            - skills: str | list, search query, search by skill(s)
            - interests: str | list, search query, search by interest(s) as a list or comma separated strings
            - location: str, search query, search by location if the user
            - timezone: str, search query, search by tinezone of the user

    RETURNS:
        - List[UserResponse]: list of user objects

    """
    token = verify_access_token(token)
    if not token:
        failure = {"error": "Invalid token", "code": "UNAUTHORIZED"}
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=failure
        )

    params = {
        "name": name, "skills": skills, "interests": interests,
        "location": location, "timezone": timezone
    }
    query = {}

    # Add only params which were passed to the query to reduce redun database perusal
    for param_key, param in params.items():
        if param:  # an empty list will return false
            query.update({param_key: param})

    users = await user_services.search_users(query)
    return users


@search_router.get("/projects/", response_model=List[ProjectResponse])
async def search_projects(
    token: str = Depends(oauth2_scheme),
    title: Annotated[Union[str , None], Query()] = None,
    created_by: Annotated[Union[str , None], Query()] = None,
    deadline: Annotated[str, Query()] = None,
    ending: Annotated[str, Query()] = None,
    created_at: Annotated[str, Query()] = None,
    starting: Annotated[str, Query()] = None,
    type: Annotated[str, Query()] = None,
    skills: Annotated[Union[List[str], str, None], Query()] = [],  # can either be passed as a list, commas sep strings or a single string, yet is optional witha default of []
    tools: Annotated[Union[List[str], str, None], Query()] = [],
    project_tools: Annotated[Union[List[str], str, None], Query()] = [],
    tags: Annotated[Union[List[str], str, None], Query()] = [],
    collaborators: Annotated[Union[List[str], str, None], Query()] = [],
    location: Annotated[str, Query()] = None,
):
    """
    Route to search for projects

    PARAMETERS:
        - token: str, access token
        QUERY PARAMETERS:
            - title: str, search query
            - created_by: str, search query
            - deadline/ending: str, search query, search by projects not yet expired/ended
            - created_at: str, search query, search by projects created from the time henceforth
            - starting: str, search query, search by projects strating from the time henceforth
            - type: str, search query, project type
            - tags: str | list, search query, comma separated tags/hashtags or a list of tags/hashtags
            - collaborators: str | list, search query, comma separated user_ids of collabees
            - location: str, search query, location of project (non-case-sensitive)
            - skills | tools | project_tools: str | list, search query, comma separated of technologues used in the project

    RETURNS:
        - List[ProjectResponse]: list of project objects

    """
    token = verify_access_token(token)
    if not token:
        failure = {"error": "Invalid token", "code": "UNAUTHORIZED"}
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=failure
        )

    params = {
        "title": title, "created_at": created_at, "created_by": created_by,  "starting": starting,
        "deadline": deadline, "ending": ending, "type": type, "tags": tags, "collaborators": collaborators,
        "project_tools": project_tools, "tools": tools, "skills": skills,  # These three refer to the same concept
        "location": location  # likewise
    }
    query = {}

    # Add only params which were passed to the query to reduce redun database perusal
    for param_key, param in params.items():
        if param:  # an empty list will return false
            query.update({param_key: param})

    projects = await project_services.search_projects(query)
    return projects
