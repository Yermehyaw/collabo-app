""""
Test auth routes

MODULES:
    - pytest: pytest fixtures, pytest, MonkeyPatch
    - fastapi.testclient: TestClient
    - app.main: app, app entry point

"""
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    """Test the "/" endpoint
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Collabo app"}