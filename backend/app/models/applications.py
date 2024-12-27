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
       - project_id: str
       NOTE: There is no applicant_id, as this can be retrieved from the token and poses a security risk 
        whereby users with the ids of other users can make a request on their behalf without their consent

       FUTURE IMPROVEMENETS:
          - message: str, message by applicant to project owner. Muar be Optional
    """
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
    application_id: str = Field(None, alias="_id")
    project_id: str
    applicant_id: str
    status: Literal["pending", "approved", "rejected"] = "pending"
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
