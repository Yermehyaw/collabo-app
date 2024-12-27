"""
Messaging websocket models
Comprise the MessageCreate, MessageResponse, and ConversationResponse models

MODULES:
    - pydantic: BaseModel
    - typing: List, Optional
    - datetime: datetime class
    - bson: ObjectId

"""
from pydantic import (
    BaseModel
)
from typing import (
    List, Optional
)
from datetime import datetime


class MessageCreate(BaseModel):
    """
    Request model to create a new message, restablishes a websocket connection and begins a new converstion or continues with an existing one

    ATTRIBUTES:
        - conversation_id: str, id of conversation
        - receiver_id: str, id of user receiving the message
        - text: str, text message to be sent
        - timestamp: str, timestamp at when message was sent/created

    """
    conversation_id: Optional[str]  # When starting a new converstion, this attr is None, but to continue an exusuting one it is mandatory
    receiver_id: str
    text: str
    timestamp: str = datetime.now().isoformat()


class MessageResponse(BaseModel):
    """
    Response model of a message served by the server to client

    ATTRIBUTES:
        - conversation_id: str, id of conversation
        - sender_id: str, id of user sending the message
        - receiver_id: str, id of user receiving the message
        - text: str, text message that was sent
        - timestamp: str, timestamp at when message was sent/created
    """
    conversation_id: str
    sender_id: str
    receiver_id: str
    text: str
    timestamp: str


class ConversationResponse(BaseModel):
    """
    Response model of a conversation history served by the sever to client

    ATTRIBUTES:
        - conversation_id: str, id of conversation
        - messages: List, list of messages in the conversation
        - created_at: str, timestamp at when the conversation begun/was created

    """
    conversation_id: str
    messages: List[MessageResponse]
    created_at: str
