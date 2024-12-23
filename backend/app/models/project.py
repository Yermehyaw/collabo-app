"""
Project model for fastapi app

MODULES:
    - typing: custom types
    - pydantic: BaseModel, Field, ConfigDict
    - datetime: datetime class
    - uuid: uuid4 class

"""
from typing import (
    Optional, List,
    Literal, Any
)
from pydantic import (
    BaseModel,
    Field,
    ConfigDict
)
from datetime import datetime
from models.application import Application
from models.invitation import Invitation


# STANDARD PROJECT DEF MODEL
class Project(BaseModel):
    """
    Defines a project obj

    ATTRIBUTES:
    - project_id: str, unique id of project
    - db_id: str
    - title: str
    - description: str
    - created_at: str
    - updated_at: str
    - created_by: str, id of user
    - deadline: str
    - collaborators: list
    - type: str
    - tags: list, keywords used to aid recommendation/feed/siggestions
    - project_location: str
    - followers: list
    
    FUTURE IMPROVEMENTS:
    - status: Literal['ongoing', 'completed', 'paused'], describes the current state of the project
    - applications: list, list of application objs
    - invitations: list, list of invitation objs
    - project_tools: list, list of technologies/tools to be used in the project

    """
    # Required attr
    project_id: Optional[str] = Field(alias='_id', default=None)
    title: str = Field(..., min_length=4, max_length=100)
    description: Optional[str] = Field(max_length=1000)
    created_by: str
    created_at: str = datetime.now().isoformat()

    # Optional attr
    updated_at: Optional[str] = None
    deadline: Optional[str] = None
    type: Optional[str] = None
    skills_required: List[str] = []  # skills required from intending collaborator/collabee
    tags: List[str] = ["#creative", "#innovative"]  # keywords used to aid recommendation/feed/suggestions
    collaborators: List[str] = []
    followers: List[str] = []
    project_location: Optional[str] = None
    applications: List[Application] = []  # list of applications from collabee to the project creator
    invitations: List[Invitation] = []  # list of invitations by the project creator to potential collabees
    model_config = ConfigDict(
        populate_by_name=True,  # permit the id alias of user_id to work
        arbitrary_types_allowed=True,  # permit the use of non-native types in model
        # Example of expected format with the min req attr in the data supposed to utilize this model
        json_scheme_extra={
            "example": {
                "title": "My new project",
                "description": "very important project",
                "created_by": "user1010",
            }
        }
    )


# UPDATE PROJECT MODEL
class ProjectUpdate(BaseModel):
    """
    Update a project model

    ATTRIBUTES:
    - title: str
    - description: str
    - updated_at: str
    - starting: str
    - ending: str
    - collaborators: list
    - type: str
    - project_location
    - project_tools: list, list of technologues/tools to be used in the project

    """
    title: Optional[str] = Field(None, min_length=4, max_length=100, default=None)
    description: Optional[str] = Field(None, max_length=1000)
    updated_at: str = datetime.now().isoformat()  # potential security issue, user shouldnt be able to manipulate update time
    deadline: Optional[str] = None
    type: Optional[str] = None
    skills_required: List[str] = []  # skills required by any intending collaborator/collabee
    collaborators: List[str] = []
    project_location: Optional[str] = None
    applications: Optional[List[Application]] = []  # list of applications from collabee to the project creator
    invitations: Optional[List[Invitation]] = []  # list of invitations by the project creator to potential collabees
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        json_encoders={ObjectId: str},  # permit the use of ObjectId type in model but serialize/deserialize it as a str
        # Example of expected format
        json_scheme_extra={
            "example": {
                "title": "My updated project",
                "description": "very very important project",
                "deadline": "2025-12-31",
            }
        }
    )


# PROJECT RETRIEVAL MODEL
class ProjectResponse(BaseModel):
    """
    Obfuscated project model hiding sensitive data

    ATTRIBUTES:
    - title: str
    - description: str
    - created_at: str
    - updated_at: str
    - created_by: str
    - deadline: str
    - collaborators: list
    - type: str
    - tags: list, keywords used to aid recommendation/feed/siggestions
    - project_location
    - project_tools: list, list of technologues/tools to be used in the project
    - followers: list

    """
    project_id: str
    title: str
    description: Optional[str]
    created_by: str
    updated_at: Optional[str]
    deadline: Optional[str]
    type: Optional[str]
    tags: Optional[list]  # List[str] is almost analogous to Optional[list] but the former is more explicit
    collaborators: Optional[List[str]]
    followers: Optional[List[str]]
    project_location: Optional[str]
    applications: Optional[List[Any]]  # list of applications from potential collabee to the project creator
    invitations: Optional[List[Any]]  # list of invitations by the project creator to potential collabees
    model_config = ConfigDict(
        # Example of expected format
        json_scheme_extra={
            "example": {
                "project_id": "project1",
                "title": "My new project",
                "description": "very important project",
                "created_by": "user1010",
                "deadline": "2025-12-31"
            }
        }
    )
