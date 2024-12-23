"""
Project Invitation services Module
Handles business logic for invitations to collaborate on a project

MODULES:
    - typing: List, Optional, Union, Dict 
    - utils.auth.jwt_handler: verify_access_token
    - db: get_collection, get collections from db client
    - bson: ObjectId

"""
from typing import (
    List,
    Optional,
    Union, Dict
)
from datetime import datetime
from models.invitations import (
    InvitationCreate, InvitationUpdate
)
from services.user import UserService
from utils.auth.jwt_handler import verify_access_token
from db import get_collection
from uuid import uuid4
from bson import ObjectId


class InvitationServices:
    """
    Invitation services class: Includes methods to send an invitation, get invitations and update an invitation.

    ATTRIBUTES:
    - collection_name: name of collection where projects are stored in db

    """
    def __init__(self):
        """Object initializing method"""
        self.collection_name = 'invitations'

    async def insertion_collection(self):
        """
        Get the invitations collection

        RETURNS:
            - collection: collection object

        """
        return await get_collection(self.collection_name)

    async def send_invitation(self, invite: InvitationCreate) -> str:
        """
        Send an invitation to a user

        PARAMETERS:
             - invite: InvitationCreate, invitation creation  obj holding prerequisite params

        RETURNS:
            - invitation_id: stringified ObjectId, id of newly created and stored project object

        """
        insertion_id = self.insertion_collection().insert_one(invite).insertion_id  # a bson ObjectId
        invitation_id = str(insertion_id)

        return invitation_id

    async def get_invitations_to_user(self, user_id: str):
        """
        Get all invitations to a user

        PARAMETERS:
            - user_id: str

        RETURNS:
            - list: invitation objs

        """
        invitations = await self.insertion_collection().find({"invitee_id": user_id}).to_list()

        return invitations

    async def update_invitation_status(self, invitation_id: str, status: str):
        """
        Update the status of an invitation

        PARAMETERS:
           - invitation_id: str, id of invitation
           - status: str

        RETURNS:
          - None
        """
        if not ObjectId.is_valid(invitation_id):
            return None  # 403 err

        update_response = await self.insertion_collection().update_one(
            {"_id": ObjectId(invitation_id)},
            {"$set": {"status": status}}
        )

        if not update_response.matched_count:
            return None  # 403 error

        return update_response.modified_count
