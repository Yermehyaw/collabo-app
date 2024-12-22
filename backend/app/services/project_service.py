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

    async def update_project(self, project_id: str, project: ProjectUpdate) -> Optional[int]:
        """
        Update a project

        PARAMETERS:
            - project_id: str, db id of the project doc
            - project: Project, sample project object to be used to update the project in the database

        RETURNS:
            - int: no of fields updated

        """
        project.updated_at = datetime.now().isoformat()
        update_response = await self.project_collection().update_one(
            {"_id": project_id},
            {"$set": project.model_dump()}
        )

        if not update_response.matched_count:
            return None # a document with req project_id was not found

        return update_response.modified_count  # no of fields changed in the modified document

    async def delete_project(self, project_id: str) -> Optional[int]:
        """
        Delete a project

        PARAMETERS:
            - project_id: str, db id of the project doc

        RETURNS:
            - int: no of projrct doc deleted
        
        """
        delete_response = await self.project_collection().delete_one({"_id": project_id})

        return delete_response.deleted_count if delete_response.deleted_count == 1 else None  # every project has a unique id, so only one project should be deleted
    
    async def search_projects(self, filters: dict) -> List[ProjectResponse]:
        """
        Search for projects

        PARAMETERS:
            - filters: dict, search filters

        RETURNS:
            - List[Project]: list of project objects

        """
        # create a custom query from the filters dict received
        query = {}
        for key, value in filters.items():
            if key == "title":
                query[key] = {"$regex": value, "$options": "i"}  # find poject with the exact tiltle, case insensitive
            
            if key == "tags":
                if isinstance(value, str):
                    query[key] = {"$in": value.split(', ')}  # if tags is a string, split it into a list of tags delineated by a whitespace folllowing a comma
                else:  # if tags is a list
                    query[key] = {"$in": value}  # search for project bearing any tag from the list of  tags passed

            if key == "type":
                query[key] = value
            
            if key == "created_at":
                query[key] = {"$gte": value}  # search for projects created on or after the date
            
            if key == "updated_at":
                query[key] = {"$lte": value}  # search for projects updated on or before the date

            if key == "starting":
                query[key] = {"$gte": value}

            if key == "ending":
                query[key] = {"$lte": value}

            if key == "created_by":
                query[key] = value

            if key == "collaborators":
                if isinstance(value, str):
                    query[key] = {"$in": value.split()}
                else:
                    query[key] = {"$in": value}

            if key == "project_location":
                query[key] = value

            if key == "project_tools":
                if isinstance(value, str):
                    query[key] = {"$in": value.split(', ')}
                else:
                    query[key] = {"$in": value}

            if key == "followers":
                if isinstance(value, str):
                    query[key] = {"$in": value.split(', ')}
                else:
                    query[key] = {"$in": value}

            # Search by invitations and applications can be implemented in the future

        projects = await self.project_collection().find(query).to_list(length=None)

        return [ProjectResponse(**project) for project in projects]
