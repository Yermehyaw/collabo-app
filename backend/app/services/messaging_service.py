"""
Mesaging websocket services
This module contains the services for the messaging websocket. It contains the logic to create, update, and delete messages and conversations.

MODULES:
    - typing: List
    - bson: ObjectId
    - models.messages: MessageCreate, MessageResponse, ConversationResponse

"""
from typing import List
from bson import ObjectId
from models.messages import (
    MessageCreate, MessageResponse, ConversationResponse
)
from user_service import UserService
from db import get_collection


class MessagingService:
    """
    Messaging websocket services class
    Contains the logic to create, update, and delete messages and conversations

    ATTRIBUTES:
        - collection: str, name of the collection in the database
        - user_service: UserService, instance of the user service class
    
    """
    def __init__(self):
        self.collection = "messages"
        self.user_service = UserService()

    async def messages_collection(self):
       """Retrieves an instance of the messages collection
       """
       return await get_collection(self.collection)

    async def receive_websocket_request(websocket):
        """
        Receives a message request

        PARAMETERS:
            - websocket: WebSocket, websocket connection

        RETURNS:
            - data: dict, request data received from the client
        """
        try:
            data = await websocket.receive_text()
            return data
        except Exception:
            return {}
        
    async def send_websocket_response(websocket, response):
        """
        Sends a response to the client

        PARAMETERS:
            - websocket: WebSocket, websocket connection
            - response: dict, response data to be sent to the client

        RETURNS:
            - Boolean, True if response was sent successfully, False otherwise
        """
        try:
            await websocket.send_text(response)
            return True
        except Exception:
            return False
    
    async def create_message(self, message: MessageCreate, conversation_id: str = None) -> str:
        """
        Creates a new message in the database

        ATTRIBUTES:
            - message: MessageCreate, obj with the req attr of MessageCreate model
            - converstion_id: str, id of conversation

        RETURNS:
            - message_id: str, id of the created message

        """
        if not conversation_id:
            conversation_id = str(ObjectId())
        message = message.dict()
        message["_id"] = conversation_id

        collection = await self.messages_collection()
        await collection.insert_one(message)

        return conversation_id
    
    async def get_conversation(self, conversation_id: str) -> List[MessageResponse]:
        """
        """
        pass
    