"""
User model for fastapi app

MODULES:
    - typing: Union class
    - pydantic: BaseModel class
    - datetime: datetime class
    - uuid: uuid4 class

"""
from typing import (
    Union,
    Optional
)
from pydantic import (
    BaseModel,
    EmailStr,
    Field,
    constr,
    validator
)
from datetime import datetime
from uuid import uuid4


# DEFINTION OF A USER
class User(BaseModel):
    """
    Users description class for creating a new user

    ATTRIBUTES:
        - name: str
        - email: str
        - password: str
        - created_at: str
        - updated_at: str
        - profile_pic: bytes
        - bio: str
        - skills: list
        - friends: list
        - collabees: list
        - objs: list
        - interests: list
        - projects: list
        - followers: list
        - following: list
        - language: str
        - location: str
        - timezone: str

    """
    user_id: str = 'user' + str(uuid4())  # unique user id
    db_id: str = None # database id of user object
    name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr
    password: str = Field(..., min_length=8)  # hashed password, real password are never stored
    created_at: str = datetime.now().isoformat()
    updated_at: str = datetime.now().isoformat()
    profile_pic: Optional[bytes] = None
    bio: Optional[str] = None
    skills: Optional[list] = None
    friends: Optional[list] = None
    collabees: Optional[list] = None  # list of users the user is currently collaborating with
    objs: Optional[list] = None
    interests: Optional[list] = None
    projects: Optional[list] = None
    followers: Optional[list] = None
    following: Optional[list] = None
    language: Optional[str] = 'eng'
    location: Optional[str] = None
    timezone: Optional[str] = 'UTC'


# RETRIEVE USER
class UserResponse(BaseModel):
    """
    Users description class for retrieving a user for responses. Only non-sensitive data should be included.

    ATTRIBUTES:
        - user_id: str
        - name: str
        - email: str
        - created_at: str
        - profile_pic: bytes
        - bio: str
        - skills: list
        - friends: list
        - collabees: list
        - objs: list
        - interests: list
        - projects: list
        - followers: list
        - following: list
        - language: str
        - location: str
        - timezone: str

    """
    user_id: str
    name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr
    created_at: str
    profile_pic: Optional[bytes] = None
    bio: Optional[str] = None
    skills: Optional[list] = None
    friends: Optional[list] = None
    collabees: Optional[list] = None  # list of users the user is currently collaborating with
    objs: Optional[list] = None
    interests: Optional[list] = None
    projects: Optional[list] = None
    followers: Optional[list] = None
    following: Optional[list] = None
    language: Optional[str] = 'eng'
    location: Optional[str] = None
    timezone: Optional[str] = 'UTC'


# USER SIGNUP
class UserSignup(User):
    """
    Users description class for signing up a new user

    ATTRIBUTES:
        - name: str
        - email: str
        - password: str

    """
    name: str
    email: EmailStr
    password: str = Field(..., min_length=8)

# USER LOGIN
class UserLogin(BaseModel):
    """
    Users description class for logging in a user

    ATTRIBUTES:
        - email: str
        - password: str
        - 

    """
    email: EmailStr
    password: str = Field(..., min_length=8)


# JWT Token RESPONSE
class Token(BaseModel):
    """
    Token description class for responses

    ATTRIBUTES:
        - access_token: str
        - token_type: str

    """
    access_token: str
    token_type: str = 'bearer' 
