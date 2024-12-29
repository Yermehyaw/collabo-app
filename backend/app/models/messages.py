"""
Messaging websocket models
Comprise the MessageCreate, MessageResponse, and ConversationResponse models

MODULES:
    - pydantic: BaseModel, Field
    - typing: List, Optional
    - datetime: datetime class
    - bson: ObjectId

"""
from pydantic import (
    BaseModel, Field
)
from typing import (
    List, Optional, Literal
)
from datetime import datetime


class MessageCreate(BaseModel):
    """
    Request model to create a new message, restablishes a websocket connection and begins a new converstion or continues with an existing one

    ATTRIBUTES:
        - receiver_id: str, id of user receiving the message
        - text: str, text message to be sent
        - timestamp: str, timestamp at when message was sent

    """
    receiver_id: str
    text: str
    timestamp: str = datetime.now().isoformat()


class MessageResponse(BaseModel):
    """
    Response model of a message served by the server to client
    Based on curremt implementation as of 29/12/2024. this model isnt necessary but was redundantly used only once in services/message_services.py

    ATTRIBUTES:
        - conversation_id: str, id of conversation
        - sender_id: str, id of user sending the message
        - receiver_id: str, id of user receiving the message
        - text: str, text message that was sent
        - timestamp: str, timestamp at when message was sent/created
    """
    sender_id: str
    receiver_id: str
    text: str
    status: Optional[Literal["sent", "delivered"]]  # It is optional because the status is set by the server after a message has been created. A "read" can be added in future improvements
    timestamp: str


class ConversationResponse(BaseModel):
    """
    Response model of a conversation history served by the sever to client

    ATTRIBUTES:
        - conversation_id: str, id of conversation
        - users: list, id of users involved in the  conversation
        - messages: List, list of messages in the conversation
        - created_at: str, timestamp at when the conversation begun/was created

    """
    conversation_id: str = Field(alias="_id")
    users: List[str]
    messages: List[MessageResponse]
    created_at: str = datetime.now().isoformat()
