"""
Application model.
Used to send and receive application requests to join a project

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


class ApplicationCreate(BaseModel):
    """
    Request model to create an application

    ATTRUBUTES:
       - application_id: str, stringified ObjectId
       - project_id: str

       FUTURE IMPROVEMENETS:
          - message: str, message by applicant to project owner. Muar be Optional
    """
    application_id: Optional[str] = Field(None, alias="_id")
    project_id: str
    model_config = ConfigDict(
        json_scheme_extra={  # example of expected model of a json request body
            "example": {
                "project_id": "projectxxxx",
            }
        }
    )


class ApplicationResponse(BaseModel):
    """
    Response/Return model of an application

    ATTRIBUTES:
       - application_id: str, stringified ObjectId
       - applicant_id: str, id of user
       - project_id: str, id of project being applied to
       - status: literal str
       - created_at: str

       FUTURE IMPROVEMENTS:
        - message: str, message by applicant to project owner

    """
    application_id: str
    project_id: str
    applicant_id: str
    status: Literal["pending", "accepted", "rejected"] = "pending"
    created_at: str = datetime.now().isoformat()
    model_config = ConfigDict(
        # populate_by_name=True,  # Not sure if this is necessary, but it allows an instance to be created with the name insteead of its alias
        json_scheme_extra={
            "example": {
                "application_id": "xxxxxc",
                "project_id": "projectxxxx",
                "applicant_id": "userxxxxxc",
                "created_at": "2025-01-01"
            }
        }
    )
