"""
Routes for project endpoints

MODULES:
    - fastapi: APIRouter, Depends, HTTPException, status
    - services.project_service: ProjectService
    - models.project: Project, ProjectUpdate, ProjectResponse
    - utils.auth.password_utils: verify_password
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
from typing_extensions import Annotated
from services.project_service import ProjectService
from models.project import (
    Project, ProjectResponse, ProjectUpdate
)
from utils.auth.jwt_handler import verify_access_token

project_router = APIRouter()
project_service = ProjectService()


@project_router.post("/create", response_model=ProjectResponse, status_code=status.HTTP_201_CREATED)
async def create_project(project: Project, token: str = Depends(verify_access_token)):
    """
    Create a new project

    ATTRIBUTES:
        - project: Project, model request

    RETURNS:
        - message: JSON dict, response message or error

    """
    project_id = await project_service.create_project(project)

    if not project_id:
        failure = {"error": "Project creation failed", "code": "BAD_REQUEST"}
        raise HTTPException(status_code=400, detail=failure)

    success = {"message": "Project created successfully", "project_id": project_id}
    return success


@project_router.get("/{project_id}", response_model=ProjectResponse)
async def get_project(project_id: str):
    """
    Get a projects by its project_id

    ATTRIBUTES:
        - project_id: str, unique id of project
    
    RETURNS:
        - project: ProjectResponse, project object
    
    """
    project = await project_service.get_project_by_id(project_id)

    if not project:
        failure = {"error": "Project not found", "code": "NOT_FOUND"}
        raise HTTPException(status_code=404, detail=failure)
    
    return project

@project_router.put("/{project_id}", response_model=dict)
async def update_project(project_id: str, project: ProjectUpdate, token: str = Depends(verify_access_token)):
    """
    Update a project

    ATTRIBUTES:
        - project_id: str, unique id of project
        - project: ProjectUpdate, model request
    
    RETURNS:
        - message: JSON dict, response message or error
    
    """
    fields_updated = await project_service.update_project(project_id, project)

    if fields_updated is None:
        failure = {"error": "Project not found", "code": "BAD_REQUEST"}
        raise HTTPException(status_code=404, detail=failure)
    
    if fields_updated == 0:
        success = {"message": "No data entries updated/created"}
    else:
        success = {"message": "Project updated successfully"}
    
    return success

@project_router.delete("/{project_id}", response_model=dict)
async def delete_project(project_id: str, token: str = Depends(verify_access_token)):
    """
    Delete a project

    ATTRIBUTES:
        - project_id: str, unique id of project
    
    RETURNS:
        - message: JSON dict, response message or error
    
    """
    deleted_project = await project_service.delete_project(project_id)

    if not deleted_project:
        failure = {"error": "Project not found", "code": "BAD_REQUEST"}
        raise HTTPException(status_code=404, detail=failure)
    
    success = {"message": "Project deleted successfully"}
    return success

@project_router.get("/{user_id}", response_model=list)
async def get_all_projects_by_user_id(user_id: str, token: str = Depends(verify_access_token)):
    """
    Get all projects by a user

    ATTRIBUTES:
        - user_id: str, unique id of the user
        - token: str, auth token
    
    RETURNS:
        - projects: List[ProjectResponse], list of project objects
    
    """
    projects = await project_service.get_all_projects_by_user_id(user_id)

    if not projects:
        failure = {"error": "No projects found", "code": "NOT_FOUND"}
        raise HTTPException(status_code=404, detail=failure)
    
    return projects
