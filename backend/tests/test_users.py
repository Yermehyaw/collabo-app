"""
Tests for users routes

MODULES:
    - fastapi.testclient: TestClient
    - app.main: app, app entry point
    - app.utils.auth.jwt_handler: create_access_token

"""
from fastapi.testclient import TestClient
from app.main import app
from app.utils.auth.jwt_handler import create_access_token


client = TestClient(app)
test_user = {"email": "test@tester.com", "password": "tester1234", "name": "Tester"}
token = create_access_token(test_user)
