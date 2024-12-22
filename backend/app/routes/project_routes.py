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
from models.project import Project, ProjectResponse, ProjectUpdate
from utils.auth.password_utils import verify_password
from utils.auth.jwt_handler import verify_access_token

project_router = APIRouter()
project_service = ProjectService()


@project_router.post("/create", response_model=ProjectResponse)
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
        failure = {}
        raise HTTPException(status_code=400, detail=failure)

    success = {}
    return success
