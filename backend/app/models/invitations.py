"""
Invitation model.
Used to send and receive invitation requests from project ownerto a potential collabee/collaborator

MODULES:
    - typing: custom types
    - pydantic: BaseModel, Field, ConfigDict
    - datetime: datetime class
    - uuid: uuid4 class

"""
from typing import (
    Optional,
    Literal
)
from pydantic import (
    BaseModel,
    Field,
    ConfigDict
)
from datetime import datetime


class InvitationCreate(BaseModel):
    """
    Request model to create an invitation

    ATTRUBUTES:
       - invitation_id: str, stringified ObjectId
       - project_id: str
       - invitee_id: str, id of user being invuted to join a project

       FUTURE IMPROVEMENETS:
          - message: str, message by applicant to project owner. Must be Optional
    """
    invitation_id: Optional[str] = Field(None, alias="_id")
    project_id: str
    invitee_id: str
    model_config = ConfigDict(
        json_scheme_extra={  # example of expected model of a json request body
            "example": {
                "project_id": "projectxxxx",
                "invitee_id": "userxxxxxc"
            }
        }
    )


class InvitationResponse(BaseModel):
    """
    Response/Return model of an invitation

    ATTRIBUTES:
       - invitation_id: str, stringified ObjectId
       - inviter_id: id of project creator
       - invitee_id: str, id of user invite is being sent to
       - project_id: str, id of project being applied to
       - status: literal str, stat of invitation
       - created_at: str

       FUTURE IMPROVEMENTS:
        - message: str, message by applicant to project owner

    """
    invitation_id: Optional[str]
    project_id: str
    inviter_id: str
    invitee_id: str
    status: Literal["pending", "accepted", "declined"] = "pending"
    created_at: str = datetime.now().isoformat()
    model_config = ConfigDict(
        # populate_by_name=True,  # Not sure if this is necessary, but it allows an instance to be created with the name insteead of its alias
        json_scheme_extra={
            "example": {
                "invitation_id": "xxxxxc",
                "project_id": "projectxxxx",
                "invitee_id": "userxxxxxa",
                "inviter_id": "userxxxxxb",
                "created_at": "2025-01-01"
            }
        }
    )
