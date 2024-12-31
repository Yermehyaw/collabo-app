"""
Messages and conversations routes

MODULES:
    - fastapi: APIRouter, WebSocket, WebSocketDisconnect, WebSocketException, HTTPException, Depends, status
    - typing: List
    - services.messaging_service: MessagingService
    - models.messages: MessageCreate, ConversationResponse
    - utils.auth.jwt_handler: verify_access_token

"""
from fastapi import (
    APIRouter, WebSocket, WebSocketDisconnect, HTTPException,
    WebSocketException, Depends
)
from typing import List
from services.messaging_service import MessagingService
from models.messages import (
    MessageCreate, ConversationResponse
)
from utils.auth.jwt_handler import verify_access_token


message_router = APIRouter()
conversation_router = APIRouter()
messaging_service = MessagingService()


@message_router.websocket("/")
async def messaging_websocket(websocket: WebSocket, token: str = Depends(verify_access_token)):
    """
    Establishes a websocket connection for messaging

    ATTRIBUTES:
        - websocket: WebSocket, websocket connection
        - token: str, JWT token
    
    """
    user_id = token["sub"]
    await messaging_service.connect(user_id, websocket)
    try:
        while True:
            # Listen for incoming messages to be sent
            message = await messaging_service.receive_message(websocket)

            # Send the message to the recipient
            await messaging_service.send_message(message)
    except (WebSocketDisconnect, WebSocketException):
        messaging_service.disconnect(user_id, websocket)


@message_router.post("/", response_model=dict)
async def offline_messaging(message: MessageCreate, token: str = Depends(verify_access_token)):
    """
    Fallback equivalent if the user could not connect to the websocket

    PARAMETERS:
        - message: MessageCreate, message creation object
        - token: str, JWT token

    RETURNS:
        - message: JSON dict, messgae response or error
    
    """
    try:
        await messaging_service.send_message(message.to_dict(), user_id=token["sub"])
        return {"message": "Message sent successfully"}
    except Exception:
        raise HTTPException(status_code=500, detail={"error": "Message could not be sent"})


@conversation_router.get("/{receiver_id}", response_model=ConversationResponse)
async def get_conversation(receiver_id: str, token: str = Depends(verify_access_token)):
    """
    Get a conversation between two users

    PARAMETERS:
        - user_id: str, id of the user/sender
        - reciever_id: str, id of the receiver
        - token: str, JWT token

    RETURNS:
        - conversation: ConversationResponse, conversation between two users
    
    """
    user_id = token["sub"]
    conversation = await messaging_service.get_conversation(user_id, receiver_id)
    return conversation


@conversation_router.get("/", response_model=List[ConversationResponse])
async def get_conversation_history(user_id: str, token: str = Depends(verify_access_token)):
    """
    Get the conversation history of a user

    PARAMETERS:
        - user_id: str, id of the user
        - token: str, JWT token

    RETURNS:
        - conversation: ConversationResponse, conversation history
    
    """
    all_conversations = await messaging_service.get_conversation_history(user_id)
    return all_conversations
