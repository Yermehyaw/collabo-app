import pytest
from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)

# Helper function for authenticated requests
def send_authenticated_request(method, url, token=None, json=None):
    """
    Helper function for sending authenticated requests to reduce redundancy.
    """
    params = {"token": token} if token else {}
    return client.request(method, url, json=json, params=params)

@pytest.fixture
def mock_valid_token():
    """
    Provides a valid mock token for use in tests requiring authentication.
    ???Replace with dynamic generation if JWT settings change???
    """
    return "mock_valid_token"

@pytest.fixture
def mock_invalid_token():
    """
    Provides an invalid JWT token for testing unauthorised access.
    """
    return "mock_invalid_token"

@pytest.fixture
def valid_application_data():
    """
    Provides valid application data payload for tests.
    """
    return {
        "project_id": "projectxxxx",
    }

@pytest.mark.parametrize(
    "token, expected_status, expected_message",
    [
        ("mock_invalid_token", 201, "Application submitted successfully"),
        ("mock_invalid_token", 401, "Invalid or expired token"),
        (None, 401, "Not authenticated")
    ],
)
def test_submit_application_with_varied_tokens(
    token, expected_status, expected_message, valid_application_data, monkeypatch
):
    """
    Tests application submission with valid, invalid, and missing tokens.
    """
    def mock_get_project_by_id(project_id):
        return {"id": project_id, "title": "Test Project", "created_by": "user123"}
    
    def mock_submit_application(application):
        return {"application_id": "applicationxxxx"}
    
    monkeypatch.setattr(
        "app.services.project_service.ProjectService.get_project_by_id",
        mock_get_project_by_id,
    )
    monkeypatch.setattr(
        "app.services.application_services.ApplicationServices.submit_application",
        mock_submit_application,
    )

    # Send request with token in query parameters
    response = send_authenticated_request(
        "POST", "/applications", token=token, json=valid_application_data
    )

    # Send request with token in query parameters
    response = send_authenticated_request(
        "POST", "/applications/", token=token, json=valid_application_data
    )

    if response.status_code == 422:
        print("Validation error details:", response.json())

    assert response.status_code == expected_status
    if response == 201:
        assert response.json() == {
            "message": expected_message,
            "application_id": "applicationxxxx",
        }
    else:
        assert response.json()["detail"] == expected_message

def test_submit_application_missing_fields(mock_valid_token):
    """
    Tests submission of an application with missing required fields.
    This ensures the API returns a 422 Unprocessable Entity error.
    """
    response = send_authenticated_request(
        "POST", "/applications/", mock_valid_token, json={}
    )

    # Assertions for missing fields
    assert response.status_code == 422
    assert "detail" in response.json()

def test_submit_application_invalid_project(mock_valid_token, valid_application_data, monkeypatch):
    """
    Tests submission of an application with an invalid project.
    Mocks the project lookup to return None simulating a non-existent project.
    """
    def mock_get_project_by_id(project_id):
        return None
    
    monkeypatch.setattr(
        "app.services.project_service.ProjectService.get_project_by_id",
        mock_get_project_by_id,
    )

    response = send_authenticated_request(
        "POST", "/applications/", mock_valid_token, json=valid_application_data
    )

    # Assertions for project not found
    assert response.status_code == 404
    assert response.json()["detail"] == {"error": "Project not found"}

def test_get_applications_to_project_success(mock_valid_token, monkeypatch):
    """
    Tests successful retrieval of applications a project.
    """
    def mock_get_project_by_id(project_id):
        return {"id": project_id, "created_by": "mock_user_id"}
    
    def mock_get_applications_to_project(project_id):
        return [{"application_id": "app1"}, {"application_id": "app2"}]
    
    monkeypatch.setattr(
        "app.services.project_service.ProjectService.get_project_by_id",
        mock_get_project_by_id
    )
    monkeypatch.setattr(
        "app.services.application_services.ApplicationServices.get_applications_to_project",
        mock_get_applications_to_project,
    )

    response = send_authenticated_request(
        "GET", "/applications/projectxxxx", mock_valid_token
    )

    # Assertions for successful retrieval
    assert response.status_code == 200
    assert response.json() == [{"application_id": "app1"}, {"application_id": "app2"}]

def test_update_application_status_success(mock_valid_token, monkeypatch):
    """
    Tests successful update of an application's status.
    """
    def mock_get_application_by_id(application_id):
        return {"invitee_id": "mock_user_id", "status": "pending"}

    def mock_update_application_status(application_id, status):
        return True

    monkeypatch.setattr(
        "app.services.application_services.ApplicationServices.get_application_by_id",
        mock_get_application_by_id,
    )
    monkeypatch.setattr(
        "app.services.application_services.ApplicationServices.update_application_by_status",
        mock_update_application_status
    )

    response = send_authenticated_request(
        "PUT",
        "/applications/appxxxx",
        mock_valid_token,
        json={"status": "approved"}
    )

    assert response.status_code == 200
    assert response.json()["message"] == "Application status updated successfully: approved"

def test_unauthorized_access_scenarios():
    """
    Tests endpoints for unauthorized access.
    """
    endpoints = [
        ("GET", "/applications/projectxxxx"),
        ("PUT", "/applications/appxxxx", {"status": "approved"})
    ]

    for method, url, *json in endpoints:
        response = client.request(method, url, json=json[0] if json else None)
        assert response.status_code == 401
        assert response.json()["detail"] == "Not authenticated"