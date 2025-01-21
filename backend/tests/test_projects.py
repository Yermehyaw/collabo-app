"""
Tests for projects routes

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
test_project = {
    "name": "Test Project",
    "description": "Test project description",
    "created_by": test_user.get("email"), # This is supposed to be the user_id
}
token = create_access_token(test_user)


def test_create_project():
    """Test the create project route
    """
    response = client.post("/projects/create", json=test_project, headers={"Authorization": f"Bearer {token}"})
    test_project["project_id"] = response.json().get("project_id")

    assert response.status_code == 201
    assert response.json().get("message") == "Project created successfully"