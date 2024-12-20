"""
Project Services Module
Handles businesds logic for Projects

MODULES:
    - typing: 
    - datetime: datetime method
    - models.project: project models
    - utils.auth.jwt_handler: verify_access_token
    - db: get_collection, get collections from db client

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


class ProjectService:
    """
    Project Services class: Includes methods to create, update, search, retrueve and delete a project from the db

    ATTRIBUTES:
    - collection_name: name of collection where projects are stored in db

    """
    def __init__(self):
        """Object initializing method"""
        self.collection_name = 'projects'

    async def create_project(self, project: Project):
        """
        Create a new project

        PARAMETERS:
             - project: Project, project object

        RETURNS:
            - Project: stored project object

        """
        # get project collection
        collection = await get_collection(self.collection_name)

        db_id = str(collection.insert_one(project.dict()).inserted_id)
        project.db_id = db_id  # bug: db_id of the project wasnt stored in the db

        return db_id
