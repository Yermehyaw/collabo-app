"""
Notification Service Module
"""
from datetime import datetime
from typing import List, Dict, Optional
from bson.objectid import ObjectId
from motor.motor_asyncio import AsyncIOMotorCollection


class NotificationService:
    """Service for managing user notifications."""

    def __init__(self, collection: AsyncIOMotorCollection):
        self.collection: AsyncIOMotorCollection = collection

    async def create_notification(
            self, user_id: str, notification_type: str, content: str) -> str:
        """
        Creates new notification for a user.

        Args:
            - user_id: ID of the user
            - notification_type: The type of notification
            - content: The notification content

        Returns:
            The inserted notification ID.
        
        Raises:
            RuntimeError: If notification creation fails.
        """
        try:
            notification: Dict[str, any] = {
                "user_id": ObjectId(user_id),
                "type": notification_type,
                "content": content,
                "is_read": False,
                "created_at": datetime.now().strftime('%Y-%m-%dT%H:%M:%S'),
            }
            result = await self.collection.insert_one(notification)
            return str(result.inserted_id)
        except Exception as e:
            raise RuntimeError(f"Error creating notification: {str(e)}")
    
    async def get_notification(
            self, user_id: str, unread_only: bool = False, limit: int = 100) -> List[Dict]:
        """
        Retrieves notifications for a user.

        Args:
            - user_id: ID of the user
            - unread_only: If to fetch only unread notifications
            - limit: Maximum number of notifications to fetch

        Returns:
            A list of notifications.
        
        Raises:
            RuntimeError: If it fails to retrieve notification.
        """
        try:
            query: Dict[str, any] = {"user_id": ObjectId(user_id)}
            if unread_only:
                query["is_read"] = False
            notifications = await self.collection.find(query).limit(limit).to_list(length=limit)
            return notifications
        except Exception as e:
            raise RuntimeError(f"Error retrieving notifications: {str(e)}")
    
    async def mark_as_read(self, notification_id: str) -> bool:
        """
        Mark a notification as read.

        Args:
            - notification_id: ID of the notification to mark as read
        
        Returns:
            True if the update was successful, otherwise False.

        Raises:
            RuntimeError: Fails to mark a notification as read.
        """
        try:
            result = await self.collection.update_one(
                {"_id": ObjectId(notification_id)},
                {"$set": {"is_read": True}},
            )
            return result.modified_count > 0
        except Exception as e:
            raise RuntimeError(f"Error marking notification as read: {str(e)}")