"""
Messages and conversations routes

MODULES:
    - fastapi: APIRouter, WebSocket, WebSocketDisconnect
    - services.messaging_service: MessagingService
    - models.messages: MessageCreate, MessageResponse, ConversationResponse
    - utils.auth.jwt_handler: verify_access_token

"""
from fastapi import (
    APIRouter, WebSocket, WebSocketDisconnect,
    WebSocketException, Depends, status
)
from services.messaging_service import MessagingService
from models.messages import (
    MessageCreate, MessageResponse, ConversationResponse
)
from utils.auth.jwt_handler import verify_access_token


message_router = APIRouter()
messaging_service = MessagingService()

@message_router.websocket("/messages/")
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
            message: MessageCreate = await messaging_service.receive_message(websocket)

            # Send the message to the recipient
            await messaging_service.send_message(message)
    except (WebSocketDisconnect, WebSocketException):
        messaging_service.disconnect(user_id, websocket)