"""
Defines a FastAPI router for managing notifications via HTTP endpoints.
It integrates the NotificationService class to handle database operations
and models defined in the application.
"""
from fastapi import APIRouter, Depends, HTTPException
from app.db import db
from app.models.notifications import Notification
from app.services.notification_service import NotificationService

router = APIRouter()
notification_service = NotificationService(db)

@router.post("/notifications/")
async def create_notification(notification: Notification):
    try:
        notification_id = await notification_service.create_notification(
            user_id=notification.user_id,
            notification_type=notification.type,
            content=notification.content,
        )
        return {"notification_id": notification_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/notifications/{user_id}")
async def get_notifications(user_id: str, unread_only: bool = False):
    try:
        notifications = await notification_service.get_notification(user_id, unread_only)
        return {"notifications": notifications}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/notifications/{notification_id}/read")
async def mark_as_read(notification_id: str):
    try:
        success = await notification_service.mark_as_read(notification_id)
        if not success:
            raise HTTPException(status_code=404, detail="Notification not found")
        return {"success": True}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))