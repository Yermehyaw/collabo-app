"""
Defines a FastAPI router for managing notifications via HTTP endpoints.
It integrates the NotificationService class to handle database operations
and models defined in the application.
"""
from fastapi import APIRouter, Depends, HTTPException, Query
from app.db import db
from app.models.notifications import Notification
from app.services.notification_service import NotificationService

router = APIRouter()

# Dependency injection for NotificationService
def get_notification_service() -> NotificationService:
    """
    Provides a NotificationService instance to the endpoints

    Returns:
        An instance of NotificationService
    """
    return NotificationService(db)

@router.post("/notifications/")
async def create_notification(
    notification: Notification,
    service: NotificationService = Depends(get_notification_service)
    ):
    """
    Creates a new notification.
    This endpoint accepts a notification object, processes it using
    NotificationService, and stores it in the database.

    Args:
        notification: The notification details provided by the user
        service: The injected NotificationService instance
    
    Returns:
        A dictionary containing the ID newly created notification.

    Raises:
        HTTPException: If the notification creation fails.
    """
    try:
        notification_id = await service.create_notification(
            user_id=notification.user_id,
            notification_type=notification.type,
            content=notification.content,
        )
        return {"notification_id": notification_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to create notification: {str(e)}")
    
@router.get("/notifications/{user_id}", response_model=dict)
async def get_notifications(
    user_id: str,
    unread_only: bool = Query(False, description="Fetch only unread notifications"),
    skip: int = Query(0, ge=0, description="Number of notifications to skip (for pagination)"),
    limit: int = Query(100, ge=1, le=100, description="Maximum number of notifications to retrieve"),
    service: NotificationService = Depends(get_notification_service)
    ):
    """
    Retrieves notification for a specific user.
    This endpoint fetches notifications from the database based on the user ID

    Args:
        user_id: ID of the user whose notifications are being retrieved
        unread_only: Boolean to filter only unread notifications
        skip: Number of notifications to skip (for pagination)
        limit: Number of notifications to retrieve
        service: The injected NotificationService instance

    Returns:
        A dictionary containing a list of notifications

    Raises:
        HTTPException: If retrieval of notifications fails.
    """
    try:
        notifications = await service.get_notification(user_id, unread_only, limit=limit)
        return {"notifications": notifications}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to retrieve notifications: {str(e)}")

@router.put("/notifications/{notification_id}/read", response_model=dict)
async def mark_as_read(
    notification_id: str,
    service: NotificationService = Depends(get_notification_service)
    ):
    """
    Marks a specific notification as read.
    This endpoint updates `is_read` status of a notification to `True`
    based on the provided notification ID.

    Args:
        notification_id: ID of the notification to mark as read
        service: The injected NotificationService instance

    Returns:
        A dictionary indicating the success status of the operation.

    Raises:
        HTTPException: If the exception is not found or the operation fails.
    """
    try:
        success = await service.mark_as_read(notification_id)
        if not success:
            raise HTTPException(status_code=404, detail="Notification not found")
        return {"success": True}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to mark notification as read: {str(e)}")