"""
fastAPI app entry point

MODULES:
    - fastapi: FastAPI class

"""
from fastapi import FastAPI
from routes.auth import auth_router

app = FastAPI()

# Map routes the fastAPI routes module
app.include_router(auth_router, tags=['Auth'])

# Run the app via uvicorn in a shell terminal
# uvicorn main:app --reload