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

        ATTRIBUTES:
            - user_id: ID of the user
            - notification_type: The type of notification
            - content: The notification content

        RETURN: The inserted notification ID
        """
        try:
            notification: Dict[str, any] = {
                "user_id": ObjectId(user_id),
                "type": notification_type,
                "content": content,
                "is_read": False,
                "created_at": datetime.now().strftime('%Y-%m-%dT%H:%H:M:%S'),
            }
            result = await self.collection.insert_one(notification)
            return str(result.inserted_id)
        except Exception as e:
            raise RuntimeError(f"Error creating notification: {str(e)}")
    
    async def get_notification(
            self, user_id: str, unread_only: bool = False, limit: int = 100) -> List[Dict]:
        """
        Retrieves notifications for a user.

        ATTRIBUTES:
            - user_id: ID of the user
            - unread_only: If to fetch only unread notifications
            - limit: Maximum number of notifications to fetch

        RETURN: A list of notifications
        """
        try:
            query: Dict[str, any] = {"user_id": ObjectId(user_id)}
            if unread_only:
                query["is_read"] = False
            notifications = await self.collection.find(query).limit(limit).to_list(lenght=limit)
            return notifications
        except Exception as e:
            raise RuntimeError(f"Error retrieving notifications: {str(e)}")
    
    async def mark_as_read(self, notification_id: str):
        """
        Mark a notification as read.

        ATTRIBUTES:
            - notification_id = ID of the notification to mark as read
        
        RETURN: True if the update was successful, otherwise False.
        """
        try:
            result = await self.collection_name.update_one(
                {"_id": ObjectId(notification_id)},
                {"$set": {"is_read": True}},
            )
            return result.modified_count > 0
        except Exception as e:
            raise RuntimeError(f"Error marking notification as read: {str(e)}")