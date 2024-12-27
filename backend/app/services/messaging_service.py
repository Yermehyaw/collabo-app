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