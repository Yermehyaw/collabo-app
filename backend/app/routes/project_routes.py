"""
Routes for project endpoints

MODULES:
    - fastapi: APIRouter, Depends, HTTPException, status
    - fastapi.security: OAuth2PasswordBearer
    - services.project_services: ProjectServices
    - models.project: Project, ProjectUpdate, ProjectResponse
    - utils.auth.jwt_handler: verify_access_token

FUTURE IMPROVEMENTS:
    - utils.auth.jwt_handler: get_current_user
    - utils.auth.jwt_handler: get_current_active_user
    - utils.auth.jwt_handler: get_current_active_superuser

"""
from fastapi import (
    APIRouter, HTTPException,
    status, Depends
)
from fastapi.security import OAuth2PasswordBearer
from services.project_services import ProjectServices
from models.projects import (
    ProjectCreate, ProjectResponse, ProjectUpdate
)
from utils.auth.jwt_handler import verify_access_token


project_router = APIRouter()
project_services = ProjectServices()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@project_router.post("/create", response_model=dict, status_code=status.HTTP_201_CREATED)
async def create_project(project: ProjectCreate, token: str = Depends(oauth2_scheme)):
    """
    Create a new project

    ATTRIBUTES:
        - project: ProjectCreate, model request
        - token: str, jwt auth token

    RETURNS:
        - message: JSON dict, response message or error

    """
    token = verify_access_token(token)  # Decode and further verify token
    if not token:
        failure = {"error": "Invalid token", "code": "UNAUTHORIZED"}
        raise HTTPException(status_code=401, detail=failure)

    user_id = token.get("sub")  # Get user_id from token
    project_id = await project_services.create_project(project, user_id)

    if not project_id:
        failure = {"error": "Project creation failed", "code": "BAD_REQUEST"}
        raise HTTPException(status_code=400, detail=failure)

    success = {"message": "Project created successfully", "project_id": project_id}
    return success


@project_router.get("/{project_id}", response_model=ProjectResponse)
async def get_project(project_id: str, token: str = Depends(oauth2_scheme)):
    """
    Get a projects by its project_id

    ATTRIBUTES:
        - project_id: str, unique id of project
        - token: str, jwt auth token
    
    RETURNS:
        - project: ProjectResponse, project object
    
    """
    token = verify_access_token(token)  # Decode and further verify token
    if not token:
        failure = {"error": "Invalid token", "code": "UNAUTHORIZED"}
        raise HTTPException(status_code=401, detail=failure)
    
    project = await project_services.get_project_by_id(project_id)

    if not project:
        failure = {"error": "Project not found", "code": "NOT_FOUND"}
        raise HTTPException(status_code=404, detail=failure)
    
    return project

@project_router.put("/{project_id}", response_model=dict)
async def update_project(project_id: str, project: ProjectUpdate, token: str = Depends(oauth2_scheme)):
    """
    Update a project

    ATTRIBUTES:
        - project_id: str, unique id of project
        - project: ProjectUpdate, model request
        - token: str, jwt auth token
    
    RETURNS:
        - message: JSON dict, response message or error

    NOTE:
        - Irrespective of whether or not the fields in the project are actually updated, the updated_at field is always updated and a success message is returned

    """
    token = verify_access_token(token)  # Decode and further verify token
    if not token:
        failure = {"error": "Invalid token", "code": "UNAUTHORIZED"}
        raise HTTPException(status_code=401, detail=failure)

    fields_updated = await project_services.update_project(project_id, project)

    if fields_updated is None:
        failure = {"error": "Project not found", "code": "BAD_REQUEST"}
        raise HTTPException(status_code=404, detail=failure)
    
    success = {"message": "Project updated successfully"}
    return success

@project_router.delete("/{project_id}", response_model=dict)
async def delete_project(project_id: str, token: str = Depends(oauth2_scheme)):
    """
    Delete a project

    ATTRIBUTES:
        - project_id: str, unique id of project
        - token: str, jwt auth token
    
    RETURNS:
        - message: JSON dict, response message or error
    
    """
    token = verify_access_token(token)  # Decode and further verify token
    if not token:
        failure = {"error": "Invalid token", "code": "UNAUTHORIZED"}
        raise HTTPException(status_code=401, detail=failure)

    deleted_project = await project_services.delete_project(project_id)

    if not deleted_project:
        failure = {"error": "Project not found", "code": "NOT_FOUND"}
        raise HTTPException(status_code=404, detail=failure)
    
    success = {"message": "Project deleted successfully"}
    return success

@project_router.get("/me/{user_id}", response_model=list)
async def get_all_projects_by_user_id(user_id: str, token: str = Depends(oauth2_scheme)):
    """
    Get all projects by a user

    ATTRIBUTES:
        - user_id: str, unique id of the user
        - token: str, auth token
    
    RETURNS:
        - projects: List[ProjectResponse], list of project objects
    
    """
    token = verify_access_token(token)  # Decode and further verify token
    if not token:
        failure = {"error": "Invalid token", "code": "UNAUTHORIZED"}
        raise HTTPException(status_code=401, detail=failure)

    projects = await project_services.get_all_projects_by_user_id(user_id)

    if not projects:
        failure = {"error": "No projects found", "code": "NOT_FOUND"}
        raise HTTPException(status_code=404, detail=failure)

    return projects
