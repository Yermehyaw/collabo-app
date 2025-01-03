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
)
from typing import List
from backend.app.services.project_services import ProjectService
from services.application_services import ApplicationServices
from models.applications import (
    ApplicationCreate, ApplicationResponse
)
from utils.auth.jwt_handler import verify_access_token


application_router = APIRouter()
application_services = ApplicationServices()
project_service = ProjectService()


@application_router.post("/", response_model=dict, status_code=status.HTTP_201_CREATED)
async def submit_application(application: ApplicationCreate, token: str = Depends(verify_access_token)):
    """
    Submit an application to a project

    ATTRIBUTES:
        - application: ApplicationCreate, obj with the req attr of ApplicationCreate model

    RETURNS:
        - message: JSON dict, response message or error

    """
    project = await project_service.get_project_by_id(application.project_id)

    if not project:
        failure = {"error": "Project not found", "code": "NOT_FOUND"}
        raise HTTPException(status_code=404, detail=failure)

    application["applicant_id"] = token["sub"]
    application_id = application_services.submit_application(application)

    if not application_id:
        failure = {"error": "Application submission failed", "code": "BAD_REQUEST"}
        raise HTTPException(status_code=400, detail=failure)

    success = {"message": "Application submitted successfully", "application_id": application_id}
    return success

@application_router.get("/{project_id}", response_model=List[ApplicationResponse])
async def get_applications_to_project(project_id: str, token: str = Depends(verify_access_token)):
    """
    Get a list of applications to a project

    ATTRIBUTES:
        - project_id: str, unique id of project
    
    RETURNS:
        - list: list of applications to a project
    
    """
    project = await project_service.get_project_by_id(project_id)

    if not project or project["created_by"] != token["sub"]:
        failure = {"error": "You are not allowed to view the applications to this project", "code": "PERMISSION_DENIED"}
        raise HTTPException(status_code=403, detail=failure)

    applications = await application_services.get_applications_to_project(project_id)

    return applications

@application_router.put("/{application_id}", response_model=dict)
async def update_application_status(status: str, application_id: str, token: str = Depends(verify_access_token)):
    """
    Update the status of an application

    PARAMETERS:
        - status: str, new status of the application
        - application_id: str, id of the application
        - token: str, jwt token

    RETURNS:
        - dict: json, message response

    """
    # validate its application_id and the request was sent by the applicant
    application = application_services.get_application_by_id(application_id)

    if not application or application.invitee_id != token["sub"]:
        failure = {"error": "You are not permitted to update this application", "code": "PERMISSION_DENIED"}
        raise HTTPException(status_code=403, detail=failure)

    updated_response = await application_services.update_application_status(application_id, status)

    if not updated_response:
        failure = {"error": "Application not found", "code": "NOT_FOUND"}
        raise HTTPException(status_code=404, detail=failure)

    success = {"message": f"Application status updated successfully: {status}"} 
    return success