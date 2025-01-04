"""
fastAPI app entry point

MODULES:
    - fastapi: FastAPI class

"""
from fastapi import FastAPI
from routes.auth_routes import auth_router
from routes.user_routes import user_router
from routes.project_routes import project_router
from routes.friend_routes import friend_router
from routes.application_routes import application_router
from routes.invitation_routes import invitation_router
from routes.search_routes import search_router
from routes.suggestion_routes import suggestion_router
from routes.message_routes import message_router
from routes.message_routes import conversation_router

# Initialize the FastAPI app
app = FastAPI()

# Homepage
app.get('/')
async def root():
    return {"message": "Welcome to the Collabo app"}

# Map other routes to the fastAPI app
app.include_router(auth_router, prefix='/auth', tags=['Auth'])
app.include_router(user_router, prefix='/users', tags=['Users'])
"""
app.include_router(project_router, prefix='/projects', tags=['Projects'])
app.include_router(friend_router, prefix='/friends', tags=['Friends'])
app.include_router(application_router, prefix='/applications', tags=['Applications'])
app.include_router(invitation_router, prefix='/invitations', tags=['Invitations'])
app.include_router(search_router, prefix='/search', tags=['Search'])
app.include_router(suggestion_router, prefix='/suggestions', tags=['Suggestions'])
app.include_router(message_router, prefix='/messages', tags=['Messages'])
app.include_router(conversation_router, prefix='/conversations', tags=['Conversations'])
"""

# Run the app via uvicorn in a shell terminal
# uvicorn main:app --reload
