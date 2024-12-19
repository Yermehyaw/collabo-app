"""
Project model for fastapi app

MODULES:
    - typing: Union class
    - pydantic: BaseModel class
    - datetime: datetime class
    - uuid: uuid4 class
    - user: User object

"""
from typing import (
    Optional,
    Union,
    List
)
from pydantic import (
    BaseModel,
    Field,
)
from datetime import datetime
from uuid import uuid4
from user import User


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
    project_id: str = 'project' + str(uuid4())
    db_id: str = None
    title: str = Field(..., min_length=4, max_length=100)
    description: Optional[str] = Field(max_length=1000)
    created_at: str = datetime.now().isoformat()
    updated_at: str = datetime.now().isoformat()
    deadline: Optional[str] = None
    creator_id: str
    type: Optional[str] = None
    tags: List[Union[str | None]] = []
    collaborators: List[Union[str | None]] = []
    followers: List[Union[str | None]] = []
    project_tools: List[Union[str | None]] = []
    project_location: Optional[str] = None


# UPDATE PROJECT MODEL
class ProjectUpdate(BaseModel):
    """
    Update a project model

    ATTRIBUTES:
    - title: str
    - description: str
    - updated_at: str
    - deadline: str
    - collaborators: list
    - type: str
    - project_location
    - project_tools: list, list of technologues/tools to be used in the project

    """
    title: str = Field(..., min_length=4, max_length=100)
    description: Optional[str] = Field(max_length=1000)
    updated_at: str = datetime.now().isoformat()
    deadline: Optional[str] = None
    type: Optional[str] = None
    collaborators: List[Union[str | None]] = []
    project_tools: List[Union[str | None]] = []
    project_location: Optional[str] = None


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
    project_id: str = 'project' + str(uuid4())
    title: str = Field(..., min_length=4, max_length=100)
    description: Optional[str] = Field(max_length=1000)
    created_at: str = datetime.now().isoformat()
    updated_at: str = datetime.now().isoformat()
    deadline: Optional[str] = None
    creator_id: str
    type: Optional[str] = None
    tags: List[Union[str | None]] = []
    collaborators: List[Union[str | None]] = []
    followers: List[Union[str | None]] = []
    project_tools: List[Union[str | None]] = []
    project_location: Optional[str] = None
