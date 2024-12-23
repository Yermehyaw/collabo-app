"""
Project Application services Module
Handles business logic for applications to collaborate on a project

MODULES:
    - db: get_collection, get collections from db client
    - bson: ObjectId
    - models.applications: application models

"""
from models.applications import (
    ApplicationCreate, ApplicationUpdate
)
from db import get_collection
from bson import ObjectId


class ApplicationServices:
    """
    Application services class: Includes methods to send an application, get applications and update an application.

    ATTRIBUTES:
    - collection_name: name of collection where projects are stored in db

    """
    def __init__(self):
        """Object initializing method"""
        self.collection_name = 'applications'

    async def applications_collection(self):
        """
        Get the applications collection

        RETURNS:
            - collection: collection object

        """
        return await get_collection(self.collection_name)

    async def submit_application(self, apply: ApplicationCreate) -> str:  # apply can be a dict as well, there is no type checking by fastapi here
        """
        Submits an application to join a project

        PARAMETERS:
             - apply: ApplicationCreate, application creation  obj holding prerequisite params

        RETURNS:
            - application_id: stringified ObjectId, id of newly created and stored project object

        """
        insertion_id = self.applications_collection().insert_one(apply).insertion_id  # a bson ObjectId
        application_id = str(insertion_id)

        return application_id

    async def get_applications_to_project(self, project_id: str):
        """
        Get all applications to a project

        PARAMETERS:
            - project_id: str

        RETURNS:
            - list: application objs

        """
        applications = await self.applications_collection().find({"project_id": project_id}).to_list()

        return applications

    async def update_application_status(self, application_id: str, status: str):
        """
        Update the status of an application

        PARAMETERS:
           - application_id: str, id of application
           - status: str

        RETURNS:
          - None
        """
        if not ObjectId.is_valid(application_id):
            return None  # 403 err

        update_response = await self.applications_collection().update_one(
            {"_id": ObjectId(application_id)},
            {"$set": {"status": status}}
        )

        if not update_response.matched_count:
            return None  # 403 error

        return update_response.modified_count
