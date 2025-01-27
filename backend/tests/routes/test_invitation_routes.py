import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.utils.auth.jwt_handler import create_access_token
from unittest.mock import patch


client = TestClient(app)


# Fixtures
@pytest.fixture
def valid_token():
    """Create a valid JWT token for testing."""
    payload = {"sub": "user123", "expires_in": 9999999999}
    return create_access_token(payload)

@pytest.fixture
def invalid_token():
    """Return an invalid JWT token."""
    return "invalid.token"

@pytest.fixture
def mock_project_services():
    """Mock the ProjectServices module."""
    with patch("app.services.project_services.ProjectServices") as mock:
        yield mock

@pytest.fixture
def mock_invitation_services():
    """Mock the InvitationServices module."""
    with patch("app.services.invitation_services.InvitationServices") as mock:
        yield mock

@pytest.fixture
def mock_user_services():
    """Mock the UserServices module."""
    with patch("app.services.user_services.UserServices") as mock:
        yield mock


# Test cases for POST /invitation/
@pytest.mark.parametrize(
    "payload, expected_status, expected_response",
    [
        (
            {"project_id": "project123", "invitee_id": "user456"},
            201,
            {"message": "Invitation sent successfully", "invitation_id": "invitation123"},
        ),
        (
            {},  # Missing payload fields
            422,
            {"detail": [{"loc": ["body", "project_id"], "msg": "field required", "type": "value_error"}]},
        ),
    ],
)
def test_send_invitation(valid_token, mock_project_services, mock_invitation_services, payload, expected_status, expected_response):
    """
    Test sending an invitation with valid and invalid payloads.
    """
    mock_project_services.get_project.return_value = {"_id": "project123", "creator_id": "user123"}
    mock_invitation_services.send_invitation.return_value = "invitation123"

    headers = {"Authorization": f"Bearer {valid_token}"}
    response = client.post("/invitation/", json=payload, headers=headers)

    assert response.status_code == expected_status
    assert response.json() == expected_response

def test_send_invitation_invalid_token(invalid_token):
    """
    Test sending an invitation with an invalid token.
    """
    payload = {"project_id": "project123", "invitee_id": "user456"}
    headers = {"Authorization": f"Bearer {invalid_token}"}
    response = client.post("/invitation/", json=payload, headers=headers)

    assert response.status_code == 401
    assert response.json()["detail"]["code"] == "UNAUTHORIZED"


# Test cases for GET /invitation/{user_id}
def test_get_invitations_to_user_valid(valid_token, mock_invitation_services, mock_user_services):
    """
    Test retrieving invitations for a valid user.
    """
    mock_user_services.get_user.return_value = {"user_id": "user123"}
    mock_invitation_services.get_invitations_to_user.return_value = [
        {
            "invitation_id": "invite1",
            "project_id": "proj1",
            "invitee_id": "user123",
            "inviter_id": "user456",
            "status": "pending",
            "created_at": "2025-01-01",
        }
    ]

    headers = {"Authorization": f"Bearer {valid_token}"}
    response = client.get("/invitation/user123", headers=headers)

    assert response.status_code == 200
    assert response.json() == mock_invitation_services.get_invitations_to_user.return_value

def test_get_invitations_to_user_unauthorized(invalid_token):
    """
    Test retrieving invitations with an invalid token.
    """
    headers = {"Authorization": f"Bearer {invalid_token}"}
    response = client.get("/invitation/user123", headers=headers)

    assert response.status_code == 401
    assert response.json()["detail"]["code"] == "UNAUTHORIZED"


# Test cases for PUT /invitation/{invitation_id}
def test_update_invitation_status_valid(valid_token, mock_invitation_services):
    """
    Test updating the status of an invitation with valid credentials.
    """
    mock_invitation_services.get_invitation_by_id.return_value = {"invitation_id": "invite123", "invitee_id": "user123"}
    mock_invitation_services.update_invitation_status.return_value = 1

    headers = {"Authorization": f"Bearer {valid_token}"}
    response = client.put("/invitation/invite123", json={"status": "accepted"}, headers=headers)

    assert response.status_code == 200
    assert response.json()["message"] == "Invitation status updated successfully: accepted"


@pytest.mark.parametrize(
    "invitation, expected_status, expected_response",
    [
        (
            None,  # Invitation not found
            404,
            {"detail": {"code": "NOT_FOUND", "message": "Invitation not found"}},
        ),
        (
            {"invitation_id": "invite123", "invitee_id": "user456"},  # Different invitee_id
            403,
            {"detail": {"code": "PERMISSION_DENIED", "message": "Permission denied"}},
        ),
    ],
)
def test_update_invitation_status_errors(valid_token, mock_invitation_services, invitation, expected_status, expected_response):
    """
    Test updating the status of an invitation with various error cases.
    """
    mock_invitation_services.get_invitation_by_id.return_value = invitation

    headers = {"Authorization": f"Bearer {valid_token}"}
    response = client.put("/invitation/invite123", json={"status": "accepted"}, headers=headers)

    assert response.status_code == expected_status
    assert response.json() == expected_response