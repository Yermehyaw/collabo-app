"""
User model for fastapi app

MODULES:
    - typing: Optional
    - pydantic: BaseModel, EmailStr, Field, ConfigDict
    - datetime: datetime class
    - uuid: uuid4 class
    - bson: ObjectId class

"""
from typing import (
    Optional
)
from pydantic import (
    BaseModel,
    EmailStr,
    Field,
    ConfigDict
)
from datetime import datetime
from uuid import uuid4
from bson import ObjectId


# DEFINTION OF A USER: USED FOR USER CREATION
class User(BaseModel):
    """
    Users description class for creating a new user. 
    Only non-sensitive data should be included during retrieval.

    ATTRIBUTES:
        - user_id: str
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
    user_id: Optional[str] = Field(alias="_id", default=None) # unique user id, same as db insertion id
    name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr
    password: str = Field(..., min_length=8)  # hashed password, real password are never stored
    created_at: str = datetime.now().isoformat()
    updated_at: Optional[str] = datetime.now().isoformat()
    profile_pic: Optional[bytes] = None
    bio: Optional[str] = None
    skills: Optional[list] = []
    friends: Optional[list] = []
    collabees: Optional[list] = []  # list of users the user is currently collaborating with
    objs: Optional[list] = []
    interests: Optional[list] = []
    projects: Optional[list] = []
    followers: Optional[list] = []
    following: Optional[list] = []
    language: Optional[str] = 'eng'
    location: Optional[str] = None
    timezone: Optional[str] = 'UTC'
    model_config = ConfigDict(
        populate_by_name=True,  # permit the id alias of user_id to work
        arbitrary_types_allowed=True,
        # Example of expected format with the min req attr in the data supposed to utilize this model
        json_scheme_extra={
            "example": {
                "name": "John Doe",
                "email": "jdoe@example.com",
                "password": "jdoepassword"
            }
        }
    )


# USER RESPONSE
class UserResponse(BaseModel):
    """
    Users description class for responses. Only non-sensitive data should be included during retrieval.

    ATTRIBUTES:
        - user_id: str
        - name: str
        - email: str
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

    """
    user_id: Optional[str] = Field(alias="_id", default=None) # unique user id, same as db insertion id
    name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr
    created_at: str = datetime.now().isoformat()
    updated_at: Optional[str] = None
    profile_pic: Optional[bytes] = None
    bio: Optional[str] = None
    skills: Optional[list] = []
    friends: Optional[list] = []
    collabees: Optional[list] = []  # list of users the user is currently collaborating with
    objs: Optional[list] = []
    interests: Optional[list] = []
    projects: Optional[list] = []
    followers: Optional[list] = []
    following: Optional[list] = []
    language: Optional[str] = 'eng'
    location: Optional[str] = None
    timezone: Optional[str] = 'UTC'
    model_config = ConfigDict(
        populate_by_name=True,  # permit the id alias of user_id to work
        arbitrary_types_allowed=True,
        # Example of expected format with the min req attr in the data supposed to utilize this model
        json_scheme_extra={
            "example": {
                "name": "John Doe",
                "email": "jdoe@example.com",
                "password": "jdoepassword"
            }
        }
    )



# UPDATE USER
class UserUpdate(BaseModel):
    """
    Users description class for updating a user for responses.

    ATTRIBUTES:
        - name: str
        - email: str
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
    name: Optional[str] = Field(..., min_length=1, max_length=100)
    email: Optional[EmailStr]
    updated_at: str = datetime.now().isoformat()
    profile_pic: Optional[bytes] = None
    bio: Optional[str] = None
    skills: Optional[list] = []
    friends: Optional[list] = []
    collabees: Optional[list] = []  # list of users the user is currently collaborating with
    objs: Optional[list] = []
    interests: Optional[list] = []
    projects: Optional[list] = []
    followers: Optional[list] = []
    following: Optional[list] = []
    language: Optional[str] = 'eng'
    location: Optional[str] = None
    timezone: Optional[str] = 'UTC'
    model_config = ConfigDict(
        arbirary_types_allowed=True,
        json_encoders={ObjectId: str},
        # Example of expected format
        json_scheme_extra={
            "example": {
                "name": "John Doe",
                "email": "jdoe@example.cpm",
                "bio": "I am a software developer",
            }
        }
    )


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
