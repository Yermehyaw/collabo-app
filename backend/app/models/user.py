"""
User model for fastapi app

MODULES:
    - typing: Union class
    - pydantic: BaseModel class
    - datetime: datetime class
    - uuid: uuid4 class

"""
from typing import Union
from pydantic import BaseModel
from datetime import datetime
from uuid import uuid4

class UserCreate(BaseModel):
    """
    Users description class for creating a new user

    ATTRIBUTES:
        - name: str
        - email: str
        - p_hash: str

    """
