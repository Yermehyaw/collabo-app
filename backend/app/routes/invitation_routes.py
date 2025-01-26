"""
Routes for invitation endpoints

MODULES:
    - fastapi: APIRouter, Depends, HTTPException, status, Body
    - fastapi.security: OAuth2PasswordBearer
    - typing: Literal
    - typing_extensions: Annotated, TypedDict
    - services.invitation_service: InvitationService
    - models.invitations: InvitationCreate, InvitationResponse
    - utils.auth.jwt_handler: verify_access_token
    - bson: ObjectId

"""
from fastapi import (
    APIRouter, HTTPException,
    status, Depends, Body
)
from fastapi.security import OAuth2PasswordBearer
from typing import Literal
from typing_extensions import (
    Annotated, TypedDict
)
from services.user_services import UserServices
from services.project_services import ProjectServices
from services.invitation_services import InvitationServices
from models.invitations import (
    InvitationCreate, InvitationResponse
)
from utils.auth.jwt_handler import verify_access_token
from bson import ObjectId


invitation_router = APIRouter()
user_services = UserServices()
project_services = ProjectServices()
invitation_services = InvitationServices()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
Status = TypedDict("Status", {"status": Literal["accepted", "rejected"]})


@invitation_router.post("/", response_model=dict, status_code=status.HTTP_201_CREATED)
async def send_invitation(invite: InvitationCreate, token: str = Depends(oauth2_scheme)):
    """
    Send an invitation to a user to join a project

    ATTRIBUTES:
        - invite: InvitationCreate, model request

    RETURNS:
        - message: JSON dict, response message or error

    """
    token = verify_access_token(token)  # Decoded token
    if not token:
        failure = {"error": "Invalid token", "code": "UNAUTHORIZED"}
        raise HTTPException(status_code=401, detail=failure)

    # Ensure its the project owner sending the request
    project = await project_services.get_project_by_id(invite.project_id)

    if not project or project["creator_id"] != token["sub"]:
        failure = {"error": "You are not permitted to send invites to other users on this project", "code": "PERMISSION_DENIED"}
        raise HTTPException(status_code=403, detail=failure)

    invite["inviter_id"] = token["sub"]
    invitation_id = await invitation_services.send_invitation(invite)

    if not invitation_id:
        failure = {"error": "Invitation failed", "code": "BAD_REQUEST"}
        raise HTTPException(status_code=400, detail=failure)

    success = {"message": "Invitation sent successfully", "invitation_id": invitation_id}
    return success


@invitation_router.get("/{user_id}", response_model=InvitationResponse)
async def get_invitations_to_user(user_id: str, token: str = Depends(oauth2_scheme)):
    """
    Get all invitations to a user

    ATTRIBUTES:
        - user_id: str, id of user
        - token: str, jwt auth token

    RETURNS:
        - invitations: list of InvitationResponse objects

    """
    token = verify_access_token(token)  # Decoded token
    if not token:
        failure = {"error": "Invalid token", "code": "UNAUTHORIZED"}
        raise HTTPException(status_code=401, detail=failure)

    # Ensure its the user requesting for their own invitations
    user = await user_services.get_user_by_id(user_id)

    if not user or user["user_id"] != user_id:
        failure = {"error": "You are not permitted to view these invitations", "code": "PERMISSION_DENIED"}
        raise HTTPException(status_code=403, detail=failure)

    # Get the invitations
    invitations = await invitation_services.get_invitations_to_user(user_id)

    return invitations

@invitation_router.put("/{invitation_id}", response_model=dict)
async def update_invitation_status(status: Annotated[Status, Body()], invitation_id: str, token: str = Depends(oauth2_scheme)):
    """
    Update the status of an invitation

    PARAMETERS:
        - status: Status, new status of the invitation
        - application_id: str, id of the invitation
        - token: str, jwt token

    RETURNS:
        - dict: json, message response

    """
    token = verify_access_token(token)  # Decoded token
    if not token:
        failure = {"error": "Invalid token", "code": "UNAUTHORIZED"}
        raise HTTPException(status_code=401, detail=failure)

    # validate its invitation_id and the request was sent by the invitee
    invitation = await invitation_services.get_invitation_by_id(invitation_id)

    if not invitation or invitation["invitee_id"] != token["sub"]:  # The conditions can be separated, the first for a 404 err and the other the 403
        failure = {"error": "You are not permitted to update this invitation", "code": "PERMISSION_DENIED"}
        raise HTTPException(status_code=403, detail=failure)

    updated_response = await invitation_services.update_invitation_status(invitation_id, status)

    if not updated_response:
        failure = {"error": "Invitation not found", "code": "NOT_FOUND"}
        raise HTTPException(status_code=404, detail=failure)

    success = {"message": f"Invitation status updated successfully: {status}"} 
    return success
