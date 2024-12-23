"""
Routes for application endpoints.
Allow usrrs to apply to become a collabee/ colloborator on a project

MODULES:
    - fastapi: APIRouter, Depends, HTTPException, status
    - services.application_services: ApplicationServices
    - models.applications: ApplicationCreate, ApplicationResponse
    - utils.auth.jwt_handler: verify_access_token

"""
from fastapi import (
    APIRouter, HTTPException,
    status, Depends
from typing import List
from services.project_service import ProjectService
from services.application_services import ApplicationServices
from models.applications import (
    ApplicationCreate, ApplicationResponse
)
from utils.auth.jwt_handler import verify_access_token


application_router = APIRouter()
application_service = ApplicationServices()
project_service = ProjectService()


@project_router.post("/", response_model=ApplicationResponse, status_code=status.HTTP_201_CREATED)
async def submit_application(application: ApplicationCreate, token: str = Depends(verify_access_token)):
    """
    Submit an application to a project

    ATTRIBUTES:
        - application: ApplicationCreate, obj with the req attr of ApplicationCreate model

    RETURNS:
        - message: JSON dict, response message or error

    """
    project = await project_service.get_project_by_id(application.application_id)

    if not project:
        failure = {"error": "Project not found", "code": "NOT_FOUND"}
        raise HTTPException(status_code=404, detail=failure)

    application_id = application_services.submit_application(application)

    if not application_id:
        failure = {}
        raise HTTPException(status_code=400, detail=failure)

    success = {"message": "Application submitted successfully", "application_id": application_id}
    return success

@project_router.get("/{project_id}", response_model=List[ApplicationResponse])
async def get_project_applications(project_id: str, token: str = Depends(verify_access_token)):
    """
    Get a list of applications to a project

    ATTRIBUTES:
        - project_id: str, unique id of project
    
    RETURNS:
        - list: list of applications to a project
    
    """
    project = await project_service.get_project_by_id(application.application_id)

    if not project:
        failure = {"error": "Project not found", "code": "NOT_FOUND"}
        raise HTTPException(status_code=404, detail=failure)

    if project["created_by"] != token["sub"]:
    failure = {}
    raise HTTPException(status_code=403, detail=failure)

    applications = await application_services.get_applications_to_project(project_id)

    return applications
