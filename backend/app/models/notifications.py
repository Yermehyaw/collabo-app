"""
Notifications model.
"""
from pydantic import BaseModel, Field, validator
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
    created_at: Optional[datetime] = Field(default_factory=datetime.now) # Ensures `created_at` is generated at runtime

    @validator("user_id")
    def validate_user_id(cls, value: str) -> str: # Custom validator
        """Custom validator that validates `user_id` to ensure consistency and correctness."""
        if len(value) != 24: # Simple validation for ObjectId length
            raise ValueError("Invalid user_id format")
        return value