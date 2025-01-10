"""
Routes for application endpoints.
Allow usrrs to apply to become a collabee/ colloborator on a project

MODULES:
    - fastapi: APIRouter, Depends, HTTPException, status, Body
    - fastapi.security: OAuth2PasswordBearer
    - typing: List, Literal
    - typing_extensions: Annotated, TypedDict
    - services.application_services: ApplicationServices
    - models.applications: ApplicationCreate, ApplicationResponse
    - utils.auth.jwt_handler: verify_access_token

"""
from fastapi import (
    APIRouter, HTTPException,
    status, Depends, Body
)
from fastapi.security import OAuth2PasswordBearer
from typing import (
    List, Literal
)
from typing_extensions import (
    Annotated, TypedDict
)
from services.project_services import ProjectServices
from services.application_services import ApplicationServices
from models.applications import (
    ApplicationCreate, ApplicationResponse
)
from utils.auth.jwt_handler import verify_access_token


application_router = APIRouter()
application_services = ApplicationServices()
project_services = ProjectServices()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
Status = TypedDict("Status", {"status": Literal["accepted", "rejected"]})


@application_router.post("/", response_model=dict, status_code=status.HTTP_201_CREATED)
async def submit_application(application: ApplicationCreate, token: str = Depends(oauth2_scheme)):
    """
    Submit an application to a project

    ATTRIBUTES:
        - application: ApplicationCreate, obj with the req attr of ApplicationCreate model

    RETURNS:
        - message: JSON dict, response message or error

    """
    token = verify_access_token(token)  # Decoded token
    if not token:
        failure = {"error": "Invalid token", "code": "UNAUTHORIZED"}
        raise HTTPException(status_code=401, detail=failure)

    project = await project_services.get_project_by_id(application.project_id)

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
async def get_applications_to_project(project_id: str, token: str = Depends(oauth2_scheme)):
    """
    Get a list of applications to a project

    ATTRIBUTES:
        - project_id: str, unique id of project
    
    RETURNS:
        - list: list of applications to a project
    
    """
    token = verify_access_token(token)  # Decoded token
    if not token:
        failure = {"error": "Invalid token", "code": "UNAUTHORIZED"}
        raise HTTPException(status_code=401, detail=failure)

    project = await project_services.get_project_by_id(project_id)

    if not project or project["created_by"] != token["sub"]:
        failure = {"error": "You are not allowed to view the applications to this project", "code": "PERMISSION_DENIED"}
        raise HTTPException(status_code=403, detail=failure)

    applications = await application_services.get_applications_to_project(project_id)

    return applications

@application_router.put("/{application_id}", response_model=dict)
async def update_application_status(status: Annotated[Status, Body()], application_id: str, token: str = Depends(oauth2_scheme)):
    """
    Update the status of an application

    PARAMETERS:
        - status: Status, new status of the application
        - application_id: str, id of the application
        - token: str, jwt token

    RETURNS:
        - dict: json, message response

    """
    token = verify_access_token(token)  # Decoded token
    if not token:
        failure = {"error": "Invalid token", "code": "UNAUTHORIZED"}
        raise HTTPException(status_code=401, detail=failure)

    # validate its application_id and the request was sent by the applicant
    application = application_services.get_application_by_id(application_id)

    if not application or application["invitee_id"] != token["sub"]:
        failure = {"error": "You are not permitted to update this application", "code": "PERMISSION_DENIED"}
        raise HTTPException(status_code=403, detail=failure)

    updated_response = await application_services.update_application_status(application_id, status)

    if not updated_response:
        failure = {"error": "Application not found", "code": "NOT_FOUND"}
        raise HTTPException(status_code=404, detail=failure)

    success = {"message": f"Application status updated successfully: {status}"} 
    return success
