""""
Test auth routes

MODULES:
    - pytest: pytest fixtures, pytest, MonkeyPatch
    - fastapi.testclient: TestClient
    - app.main: app, app entry point
    - app.utils.auth.jwt_handler: create_access_token

"""
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.utils.auth.jwt_handler import create_access_token

client = TestClient(app)
test_user = {"email": "test@tester.com", "password": "tester1234", "name": "Tester"}
token = create_access_token(test_user)

def test_root():
    """Test the "/" endpoint
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Collabo app"}

def test_signup():
    """Tests the user signup authentication
    """
    response = client.post("/auth/signup", json=test_user)
    assert response.status_code == 201
    assert response.json().get("message") == "User registered successfully"

    # Try creating the same user again
    response = client.post("/auth/signup", json=test_user)
    assert response.status_code == 400
    assert response.json().get("error") == "User already exists"
    
def test_login():
    """Tests the login authentication
    """
    response = client.post("/auth/login", json={"email": "test@tester.com", "password": "tester1234"})
    assert response.status_code == 200
    assert response.json().get("access_token") is not None
    assert response.json().get("token_type") == "bearer"

    # Incorrect login info
    response = client.post("/auth/login", json={"email": "test@tester.com", "password": "incorrecttester"})
    assert response.status_code == 401
    assert response.json().get("error") == "Invalid email or password"
