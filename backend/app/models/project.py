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
    Optional,
    List
)
from pydantic import (
    BaseModel,
    Field,
    ConfigDict
)
from datetime import datetime
from bson import ObjectId


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
    - creator_id: str
    - deadline: str
    - collaborators: list
    - type: str
    - tags: list, keywords used to aid recommendation/feed/siggestions
    - project_location
    - project_tools: list, list of technologues/tools to be used in the project
    - followers: list

    """
    project_id: Optional[str] = Field(alias='_id', default=None)
    title: str = Field(..., min_length=4, max_length=100)
    description: Optional[str] = Field(max_length=1000)
    created_by: str
    created_at: str = datetime.now().isoformat()
    updated_at: Optional[str] = None
    starting: Optional[str] = None
    ending: Optional[str] = None
    type: Optional[str] = None
    tags: List[str] = []
    collaborators: List[str] = []
    followers: List[str] = []
    project_tools: List[str] = []
    project_location: Optional[str] = None
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
    starting: Optional[str] = None
    ending: Optional[str] = None
    type: Optional[str] = None
    collaborators: List[str] = []
    project_tools: List[str] = []
    project_location: Optional[str] = None
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
    created_by: str
    created_at: str
    updated_at: Optional[str]
    starting: Optional[str]
    ending: Optional[str]
    type: Optional[str]
    tags: List[str]  # List[str] is almost analogous to Optional[list] but the former is more explicit
    collaborators: List[str]
    followers: List[str]
    project_tools: List[str]
    project_location: Optional[str]
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
