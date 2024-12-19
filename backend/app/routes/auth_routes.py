"""
Authentication routes

MODULES:
    - fastapi: APIRouter, Depends, HTTPException, status
    - services.auth_service: AuthService
    - models.user: UserSignup, UserLogin, Token
    - utils.auth.jwt_handler: create_access_token  

"""
from fastapi import (
    APIRouter, 
    Depends, 
    HTTPException, 
    status
)
from services.auth_service import AuthService
from models.user import (
    UserSignup,
    UserLogin,
    Token
)
from utils.auth.jwt_handler import (
    create_access_token
)

auth_router = APIRouter()
auth_service = AuthService()

@auth_router.post("/signup", response_model=dict)
async def signup(user: UserSignup):
    """
    Route to create a new user

    PARAMETERS:
        - user: UserSignup, user object

    RETURNS:
        - dict: newly created user object

    """
    try:
        user = await auth_service.create_user(user)
        success = {"message": "User registered successfully", "user": user.user_id}
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
    user = await auth_service.authenticate_user(user.email, user.password)
    if not user:
        failure = {"error": "Invalid email or password", "code": "UNAUTHORIZED"}
        raise HTTPException(status_code=401, detail=failure)
    
    access_token = create_access_token(data={"sub": user.user_id, "email": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
