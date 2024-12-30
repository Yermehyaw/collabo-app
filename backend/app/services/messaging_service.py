"""
Mesaging websocket services
This module contains the services for the messaging websocket. It contains the logic to create, update, and delete messages and conversations.

MODULES:
    - fastapi: WebSocket, WebSocketDisconnect, WebSocketException
    - websockets.exceptions: ConnectionClosedError
    - typing: List
    - uuid: uuid4
    - datetime: datetime
    - models.messages: MessageCreate, MessageResponse, ConversationResponse

"""
from fastapi import (
    WebSocket, WebSocketDisconnect, WebSocketException
)
from websockets.exceptions import ConnectionClosedError
from typing import (
    List, Dict
)
from uuid import uuid4
from datetime import datetime
from models.messages import (
    MessageCreate, MessageResponse, ConversationResponse
)
from db import get_collection


class MessagingService:
    """
    Messaging websocket services class
    Contains the logic to send and receive messages and conversations

    ATTRIBUTES:
        - collection: str, name of the collection in the database
        - active_connections: dict, a dict of active connections, key is the user_id and value is the websocket connection

    FUTURE IMPROVEMENTS:
        - Add a method to notify a user when he receives a message    
        - Add a method to delete a message
        - Pagination support for conversation history
    
    """
    def __init__(self):
        self.active_connections: Dict[str, WebSocket] = {}  #  A dict of active connections, key is the user_id and value is the websocket connection
        self.collection = "conversations"

    async def connect(self, user_id: str, websocket):
        """
        Connects a user to a websocket connection and stores the connection as an active connection

        PARAMETERS:
            - user_id: str, id of the user
            - websocket: WebSocket, websocket connection

        """
        await websocket.accept()
        self.active_connections[user_id] = websocket

    async def disconnect(self, user_id: str, websocket: WebSocket):
        """
        Disconnects a user from a websocket connection by removing the user from the active connections dict

        PARAMETERS:
            - user_id: str, id of the user
            - websocket: WebSocket, websocket connection
        """
        self.active_connections.pop(user_id, None)  # remove the user from the active connections but if the user wasnt even connected the pop method will return None (KeyError silenced)
        websocket.close()  # close the websocket connection

    async def send_message(self, message: dict, user_id: str):
        """
        Sends a message via a websocket connection to a receiver

        PARAMETERS:
            - message: dict, obj with the req attr of MessageCreate model, contains the text message to be sent
            - user_id: str, id of the user sending the message
        
        """
        message["sender_id"] = user_id
        
        text = message.get("text")
        receiver_id = message.get("receiver_id")
        
        if text and receiver_id in self.active_connections:
            message["status"] = "delivered"  # message was sent and seen by receipient
            await self.store_message(message)
            await self.active_connections[receiver_id].send_json(text)
        else:       
            message["status"] = "sent" # message was sent but not yet seen by receipient
            await self.store_message(message)

    async def receive_message(self, websocket: WebSocket):
        """
        Receives a message from a websocket connection

        PARAMETERS:
            - websocket: WebSocket, websocket connection

        RETURNS:
            - message: json dict, message to be sent
        """
        try:
            message = await websocket.receive_json()
            
            # Store the message in the database
            message["status"] = "delivered"
            message["timestamp"] = datetime.now().isoformat()
            return message

        except (ConnectionClosedError, WebSocketException):
            raise WebSocketDisconnect
    
    async def store_message(self, message: dict):
        """
        Stores a message in the database

        PARAMETERS:
            - message: dict, obj with the req attr of MessageCreate model, contains the text message to be stored

        """
        collection = await get_collection(self.collection)

        sender_id = message["sender_id"]
        receiver_id = message["receiver_id"]

        # Update the conversation with the new message
        updated = await collection.update_one(
            {"users": {"$all": [sender_id, receiver_id]}},  # Doc that contains both users as sending/receiving parties
            {"$push": {"messages": message}},
        )
        
        # If the conversation never existed
        if updated.matched_count == 0 and updated.modified_count == 0:
            # Create a new conversation
            conversation_id = "conv" + str(uuid4())
            conversation = ConversationResponse(
                conversation_id=conversation_id,
                users=[message["sender_id"], message["receiver_id"]],
                messages=[MessageResponse(**message)],  # redundant
                created_at=message["timestamp"]
            )
            await collection.insert_one(conversation.dict(by_alias=True))

    async def get_conversation(self, user_id: str, receiver_id: str) -> dict:
        """
        Get the conversation between two user

        PARAMETERS:
            - user_id: str, id of user who is also the sender
            - receiver_id: str, id of receipient

        RETURNS:
            - dict, conversation dict
        
        """
        collection = await get_collection(self.collection)
        conversation = await collection.find_one({"users": {"$all": [user_id, receiver_id]}})  # _id is the id attr name rather than conversation_id, not a valid ConversationResponse

    async def get_user_conversation_history(self, user_id: str) -> List[dict]:
        """
        Get all the conversations of a user

        PARAMETERS:
            - user_id: str, id of a user

        RETURNS:
            - List: list, list of conversations from db
        
        """
        collection = await get_collection(self.collection)
        return await collection.find({"users": user_id}).to_list()