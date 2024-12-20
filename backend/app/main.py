"""
fastAPI app entry point

MODULES:
    - fastapi: FastAPI class

"""
from fastapi import FastAPI
from routes.auth_routes import auth_router
from routes.user_routes import user_router

app = FastAPI()

# Map routes the fastAPI routes module
app.include_router(auth_router, prefix='/auth', tags=['Auth'])
app.include_router(user_router, prefix='/user', tags=['User'])

# Homepage
app.get('/')
async def root():
    return {"message": "Welcome to the FastAPI app"}

# Run the app via uvicorn in a shell terminal
# uvicorn main:app --reload