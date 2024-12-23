"""
Project Invitation services Module
Handles business logic for invitations to collaborate on a project

MODULES:
    - db: get_collection, get collections from db client
    - bson: ObjectId
    - models.invitations: invitation models

"""
from models.invitations import (
    InvitationCreate, InvitationUpdate
)
from db import get_collection
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

    async def invitations_collection(self):
        """
        Get the invitations collection

        RETURNS:
            - collection: collection object

        """
        return await get_collection(self.collection_name)

    async def send_invitation(self, invite: dict) -> str:
        """
        Send an invitation to a user

        PARAMETERS:
             - invite: dict, holding prerequisite params namely invitee_id, project_id, and inviter_id

        RETURNS:
            - invitation_id: stringified ObjectId, id of newly created and stored project object

        """
        insertion_id = self.invitations_collection().insert_one(invite).insertion_id  # a bson ObjectId
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
        invitations = await self.invitations_collection().find({"invitee_id": user_id}).to_list()

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

        update_response = await self.invitations_collection().update_one(
            {"_id": ObjectId(invitation_id)},
            {"$set": {"status": status}}
        )

        if not update_response.matched_count:
            return None  # 403 error

        return update_response.modified_count
