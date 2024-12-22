"""
Project model for fastapi app

MODULES:
    - typing: custom types
    - pydantic: BaseModel, Field, ConfigDict
    - datetime: datetime class
    - uuid: uuid4 class
    - user: User object

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
from bson import ObjectId
from models.user import UserResponse
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
    - creator: UserResponse, user object
    - deadline: str
    - status: Literal, either 'ongoing', 'completed', or 'paused'
    - collaborators: list
    - type: str
    - tags: list, keywords used to aid recommendation/feed/siggestions
    - project_location
    - project_tools: list, list of technologues/tools to be used in the project
    - followers: list
    - applications: list, list of application objs
    - invitations: list, list of invitation objs

    """
    project_id: Optional[str] = Field(alias='_id', default=None)
    title: str = Field(..., min_length=4, max_length=100)
    description: Optional[str] = Field(max_length=1000)
    creator: UserResponse
    created_at: str = datetime.now().isoformat()
    updated_at: Optional[str] = None
    deadline: Optional[str] = None
    type: Optional[str] = None
    skills_required: List[str] = []  # skills required by any intending collaborator/collabee
    status: Literal['ongoing', 'completed', 'paused'] = 'ongoing'
    tags: List[str] = []
    collaborators: List[str] = []
    followers: List[str] = []
    project_location: Optional[str] = None
    applications: List[Application] = []  # list of applications from collabee to the project creator
    invitations: List[Invitation] = []  # list of invitations by the project creator to potential collabees
    """
    FUTURE IMPROVEMENTS:
    starting: Optional[str] = None
    ending: Optional[str] = None
    project_tools: List[str] = []  # list of technologies/tools to be used in the project
    """
    model_config = ConfigDict(
        populate_by_name=True,  # permit the id alias of user_id to work
        arbitrary_types_allowed=True,  # permit the use of non-native types in model
        # Example of expected format with the min req attr in the data supposed to utilize this model
        json_scheme_extra={
            "example": {
                "title": "My new project",
                "description": "very important project",
                "created_by": "user1010"
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
    updated_at: str = datetime.now().isoformat()
    deadline: Optional[str] = None
    type: Optional[str] = None
    skills_required: List[str] = []  # skills required by any intending collaborator/collabee
    status: Literal['ongoing', 'completed', 'paused'] = 'ongoing'
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
                "starting": "2025-01-01",
                "ending": "2025-12-31",
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
    - creator_id: str
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
    creator: UserResponse
    updated_at: Optional[str]
    deadline: Optional[str]
    type: Optional[str]
    tags: Optional[list]  # List[str] is almost analogous to Optional[list] but the former is more explicit
    collaborators: Optional[List[str]]
    followers: Optional[List[str]]
    project_location: Optional[str]
    applications: Optional[List[Any]]  # list of applications from collabee to the project creator
    invitations: Optional[List[Any]]  # list of invitations by the project creator to potential collabees
    model_config = ConfigDict(
        # Example of expected format
        json_scheme_extra={
            "example": {
                "project_id": "project1",
                "title": "My new project",
                "description": "very important project",
                "created_by": "user1010",
                "starting": "2025-01-01",
                "ending": "2025-12-31"
            }
        }
    )
