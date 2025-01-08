"""
Project Invitation services Module
Handles business logic for invitations to collaborate on a project

MODULES:
    - db: get_collection, get collections from db client
    - bson: ObjectId
    - datetime: datetime

"""
from db import get_collection
from bson import ObjectId
from datetime import datetime


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
        return 

    async def send_invitation(self, invite: dict) -> str:
        """
        Send an invitation to a user

        PARAMETERS:
             - invite: dict, holding prerequisite params namely invitee_id, project_id and inviter_id

        RETURNS:
            - invitation_id: stringified ObjectId, id of newly created and stored project object

        """
        collection = await get_collection(self.collection_name)

        # Add the additional params req to create an InvitationResponse during response creation
        # project_id, invitee_id and inviter_id should already be in the dict
        invite["created_at"] = datetime.now().isoformat()
        invite["status"] = "pending"
        
        insertion_id = await collection.insert_one(invite.model_dump(by_alias=True))  # the invitation_id is aliased to _id so that the db auto assigns it
        invitation_id = str(insertion_id.inserted_id)

        return invitation_id
    
    async def get_invitation_by_id(self, invitation_id: str):
        """
        Get an invitation by its id

        PARAMETERS:
            - invitation_id: str

        RETURNS:
            - invitation: invitation obj

        """
        if not ObjectId.is_valid(invitation_id):
            return None

        invitation = await self.invitations_collection().find_one({"_id": ObjectId(invitation_id)})

        return invitation


    async def get_invitations_to_user(self, user_id: str):
        """
        Get all invitations to a user

        PARAMETERS:
            - user_id: str

        RETURNS:
            - list: invitation objs

        """
        cursor = self.invitations_collection().find({"invitee_id": user_id})
        invitations = await cursor.to_list(length=None)

        for invitation in invitations:
            invitation["invitation_id"] = invitation.pop("_id")

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
            return None

        update_response = await self.invitations_collection().update_one(
            {"_id": ObjectId(invitation_id)},
            {"$set": {"status": status}}
        )

        if not update_response.matched_count:
            return None

        return update_response.modified_count
