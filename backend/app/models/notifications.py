"""
Notifications model.
"""
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Notification(BaseModel):
    """
    Defines a notification object.
    """
    user_id: str
    type: str # ??Use Enum to define acceptable notification types??
    content: str
    is_read: Optional[bool] = False
    created_at: str = datetime.now().isoformat()


class FriendRequestNotification(Notification):
    """
    Defines a friend request notification, extending the
    base Notification class.
    """
    sender_id: str
    receiver_id: str