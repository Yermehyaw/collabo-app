"""
Project Application services Module
Handles business logic for applications to collaborate on a project

MODULES:
    - db: get_collection, get collections from db client
    - bson: ObjectId
    - datetime: datetime

"""
from db import get_collection
from bson import ObjectId
from datetime import datetime


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

    async def submit_application(self, apply: dict) -> str:
        """
        Submits an application to join a project

        PARAMETERS:
             - apply: ApplicationCreate/dict, application creation  obj holding prerequisite param(s) namely project_id

        RETURNS:
            - application_id: stringified ObjectId, id of newly created and stored project object

        """
        # Add the additional params req to create an ApplicationResponse during response creation
        apply["created_at"] = datetime.now().isoformat()
        apply["status"] = "pending"

        # Insert the dict into the db, the 3 other attrs req to create a valid ApplicationResponse namely, application_id, project_id and applicant_id are still missing
        insertion_id = self.applications_collection().insert_one(apply.model_dump(by_alias=True)).insertion_id  # the application_id is aliased to _id so that the db auto assigns it
        application_id = str(insertion_id)

        return application_id  # this is the application_id to be used in creating the obj in the corresp. route

    async def get_application_by_id(self, application_id: str):
        """
        Get an application by its id

        PARAMETERS:
            - application_id: str

        RETURNS:
            - application: application obj

        """
        if not ObjectId.is_valid(application_id):
            return None

        application = await self.applications_collection().find_one({"_id": ObjectId(application_id)})

        return application

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