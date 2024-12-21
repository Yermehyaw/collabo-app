"""
Notifiaction model for fastapi app

MODULES:
    - pydantic: BaseModel
"""
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Notification(BaseModel):
    """
    Defines a notification object
    """
    user_id: str
    type: str
    content: str
    is_read: Optional[bool] = False
    created_at: Optional[datetime] = datetime.now().isoformat()