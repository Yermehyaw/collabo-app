"""
Project Services Module
Handles businesds logic for Projects

MODULES:
    - typing: List, Optional, Union, Dict 
    - datetime: datetime method
    - models.project: project models
    - utils.auth.jwt_handler: verify_access_token
    - db: get_collection, get collections from db client
    - uuid: uuid4 method

"""
from typing import (
    List,
    Optional,
    Union, Dict
)
from datetime import datetime
from models.project import (
    Project, ProjectUpdate, ProjectResponse
)
from utils.auth.jwt_handler import verify_access_token
from db import get_collection
from uuid import uuid4


class ProjectService:
    """
    Project Services class: Includes methods to create, update, search, retrueve and delete a project from the db

    ATTRIBUTES:
    - collection_name: name of collection where projects are stored in db

    """
    def __init__(self):
        """Object initializing method"""
        self.collection_name = 'projects'

    async def project_collection(self):
        """
        Get the project collection

        RETURNS:
            - collection: collection object

        """
        return await get_collection(self.collection_name)

    async def create_project(self, project: Project) -> str:
        """
        Create a new project

        PARAMETERS:
             - project: Project, project object

        RETURNS:
            - project_id: id of newly created and stored project object

        """
        # convert project to a dict ready for insertion
        project_data = project.model_dump(by_alias=True)
        new_id = 'project' + str(uuid4())
        project_data['_id'] = new_id
        
        # insert project into db
        insertion_id = self.project_collection().insert_one(
            project_data
        ).inserted_id
        
        return new_id if insertion_id == new_id else None # insertion_id should be the same as new_id, just me playing around ;)
    
    async def get_project_by_id(self, project_id: str) -> Optional[ProjectResponse]:
        """
        Get a project by id

        ATTRIBUTES:
            - project_id: str, unique id of the project

        RETURNS:
            - Project: coresponding project object
        
        """
        project = await self.project_collection().find_one({"_id": project_id})

        if project:
            return ProjectResponse(**project)
        return None

    async def get_all_projects_by_user_id(self, user_id: str) -> List[ProjectResponse]:
        """
        Get all projects by a user

        ATTRIBUTES:
            - user_id: str, unique id of the user

        RETURNS:
            - List[Project]: list of project objects
        """

        projects = await self.project_collection().find({"created_by": user_id}).to_list(length=None)

        return [ProjectResponse(**project) for project in projects]
