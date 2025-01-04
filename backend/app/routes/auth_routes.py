"""
Authentication routes

MODULES:
    - fastapi: APIRouter, Depends, HTTPException, status
    - services.auth_service: AuthService
    - models.users: UserSignup, UserLogin, Token

"""
from fastapi import (
    APIRouter, 
    HTTPException, 
    status
)
from services.auth_services import AuthServices
from models.users import (
    UserSignup,
    UserLogin,
    Token
)


auth_router = APIRouter()
auth_services = AuthServices()


@auth_router.post("/signup", response_model=dict, status_code=status.HTTP_201_CREATED)
async def signup(user: UserSignup):
    """
    Route to create a new user

    PARAMETERS:
        - user: UserSignup, user object

    RETURNS:
        - dict: newly created user object

    """
    try:
        user_id = await auth_services.create_user(user)
        success = {"message": "User registered successfully", "user": user_id}
        return success
    except ValueError:
        failure = {"error": "User already exists", "code": "BAD_REQUEST"}
        raise HTTPException(status_code=400, detail=failure)
    
@auth_router.post("/login", response_model=Token)
async def login(user: UserLogin):
    """
    Route to authenticate a user

    PARAMETERS:
        - user: UserLogin, user object specifcation for login

    RETURNS:
        - Token: access token

    """
    token = await auth_services.authenticate_user(user.email, user.password)
    if not token:
        failure = {"error": "Invalid email or password", "code": "UNAUTHORIZED"}
        raise HTTPException(status_code=401, detail=failure)
    
    return token
