"""
Project Services Module
Handles business logic for Projects

MODULES:
    - typing: List, Optional
    - datetime: datetime method
    - models.project: project models
    - services.user_services: user manipulation mthds
    - utils.auth.jwt_handler: verify_access_token
    - db: get_collection, get collections from db client
    - uuid: uuid4 method

"""
from typing import (
    List,
    Optional,
)
from datetime import datetime
from models.projects import (
    ProjectCreate, ProjectUpdate, ProjectResponse
)
from services.user_services import UserServices
from utils.auth.jwt_handler import verify_access_token
from db import get_collection
from uuid import uuid4


user_services = UserServices()


class ProjectServices:
    """
    Project Services class: Includes methods to create, update, search, retrueve and delete a project from the db

    ATTRIBUTES:
    - collection_name: name of collection where projects are stored in db

    """
    def __init__(self):
        """Object initializing method"""
        self.collection_name = 'projects'

    async def create_project(self, project: ProjectCreate, user_id: str) -> str:
        """
        Create a new project

        PARAMETERS:
             - project: Project, ProjectCreate object
             - user_id: str, id of the user creating the project

        RETURNS:
            - project_id: id of newly created and stored project object

        """
        collection = await get_collection(self.collection_name)
        
        # Assert the user_id is valid
        user = await user_services.get_user_by_id(user_id)
        if not user:  # Faulty user_id was passed in the dict used to create a project
            return None

        # convert project to a dict ready for insertion
        project_data = project.model_dump(by_alias=True)
        project_data["_id"] = 'project' + str(uuid4())  # Specify what I want the insertion and return id to be
        project_data["created_by"] = user_id

        # insert project into db
        insertion = await collection.insert_one(project_data)
        insertion_id = insertion.inserted_id

        # Add the newly created project to user obj attrs
        user.projects.append(insertion_id)  # insertion_id is the same as the project_id
        user_services.update_user(user_id, user)

        # return new project id
        return insertion_id
    
    async def get_project_by_id(self, project_id: str) -> Optional[ProjectResponse]:
        """
        Get a project by id

        ATTRIBUTES:
            - project_id: str, unique id of the project

        RETURNS:
            - Project: coresponding project object
        
        """
        collection = await get_collection(self.collection_name)

        project = await collection.find_one({"_id": project_id})

        if project:
            project["project_id"] = project.pop("_id")
            return ProjectResponse(**project)
        return None

    async def get_all_projects_by_user_id(self, user_id: str) -> List[ProjectResponse]:
        """
        Get all projects by a user.
        NOTE: This method is not the only way to get all projects by a user. An alternative way would be to retrieve the projetcts from a list of project ids in the user object and then get the projects by their ids.
        However for the sake of MVP and build-time considerations, lol... Let it be so for nw

        ATTRIBUTES:
            - user_id: str, unique id of the user

        RETURNS:
            - List[Project]: list of project objects
        """
        collection = await get_collection(self.collection_name)

        cursor = collection.find({"created_by": user_id})
        projects = await cursor.to_list(length=None)

        for project in projects:
            project["project_id"] = project.pop("_id")
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
        collection = await get_collection(self.collection_name)

        update_data = project.model_dump(exclude_unset=True)  # exclude fields which are None

        list_fields = {}
        other_fields = {}
        for key, value in update_data.items():
            if isinstance(key, list):
                list_fields.update({key: value})
            else:  # key is a string, int or any other type
                other_fields.update({key: value})

        update_response = await collection.update_one(
            {"_id": project_id},
            {
                "$addToSet": list_fields,
                "$set": other_fields
            }
        )

        if update_response.matched_count == 0:
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
        collection = await get_collection(self.collection_name)

        delete_response = await collection.delete_one({"_id": project_id})

        return delete_response.deleted_count if delete_response.deleted_count == 1 else None  # every project has a unique id, so only one project should be deleted

    async def search_projects(self, filters: dict) -> list:
        """
        Search for projects

        PARAMETERS:
            - filters: dict, search filters

        RETURNS:
            - list: list of project objects

        """
        collection = await get_collection(self.collection_name)

        # create a custom query from the filters dict received
        query = {}
        for key, value in filters.items():
            if key == "title":
                query[key] = {"$regex": value, "$options": "i"}

            if key == "created_by":
                query[key] = value

            if key == "deadline":
                query[key] = {"$lte": value}

            if key == "ending":
                query[key] = {"$lte": value}

            if key == "created_at":
                query[key] = {"$gte": value}

            if key == "starting":
                query[key] = {"$gte": value}

            if key == "type":
                query[key] = value

            # Can be made case-insensitive in future improvements
            if key == "tags":
                if isinstance(value, str):
                    query[key] = {"$in": value.split(', ')}
                else:
                    query[key] = {"$in": value}

            if key == "collaborators":
                if isinstance(value, str):
                    query[key] = {"$in": value.split(', ')}
                else:
                    query[key] = {"$in": value}

            if key == "location":
                query[key] = {"$regex": value, "$options": "i"}

            # Can be made case-inssnsitive in future improvements
            if key == "project_tools" or key == "tools" or key == "skills":
                if isinstance(value, str):
                    query[key] = {"$in": value.split(', ')}
                else:
                    query[key] = {"$in": value}

        projects = await collection.find(query).to_list(length=None)
        for project in projects:
            project["project_id"] = project.pop("_id")
        return [ProjectResponse(**prj) for prj in projects]
