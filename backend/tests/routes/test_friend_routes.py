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
    payload = {
        "sub": "user123",
        "expires_in": 9999999999,
    }
    return create_access_token(payload)

@pytest.fixture
def invalid_token():
    """Return an invalid token."""
    return "invalid.token"

@pytest.fixture
def mock_friend_services():
    """Mock the FriendServices module."""
    with patch("app.services.friend_services.FriendServices") as mock:
        yield mock

@pytest.fixture
def mock_user_services():
    """Mock the UserServices module."""
    with patch("app.services.user_services.UserServices") as mock:
        yield mock


# Test cases for POST /friends/requests
@pytest.mark.parametrize(
    "payload, expected_status, expected_response",
    [
        ({"recipient_id": "user456"}, 201, {"message": "Request sent successfully", "request_id": "request123"}),
        ({}, 422, {"detail": [{"loc": ["body", "recipient_id"], "msg": "field required", "type": "value_error"}]}),  # Missing field
    ],
)
def test_send_friend_request(valid_token, mock_friend_services, payload, expected_status, expected_response):
    """
    Test sending a friend request with valid and invalid payloads.
    """
    mock_friend_services.send_friend_request.return_value = "request123"

    headers = {"Authorization": f"Bearer {valid_token}"}
    response = client.post("/friends/requests", json=payload, headers=headers)

    assert response.status_code == expected_status
    assert response.json() == expected_response

def test_send_friend_request_invalid_token(invalid_token):
    """
    Test sending a friend request with an invalid token.
    """
    payload = {"recipient_id": "user456"}
    headers = {"Authorization": f"Bearer {invalid_token}"}
    response = client.post("/friends/requests", json=payload, headers=headers)

    assert response.status_code == 401
    assert response.json()["detail"]["code"] == "UNAUTHORIZED"

def test_send_friend_request_already_exists(valid_token, mock_friend_services):
    """
    Test sending a friend request when the request already exists.
    """
    mock_friend_services.send_friend_request.return_value = None

    payload = {"recipient_id": "user456"}
    headers = {"Authorization": f"Bearer {valid_token}"}
    response = client.post("/friends/requests", json=payload, headers=headers)

    assert response.status_code == 400
    assert response.json()["detail"]["code"] == "BAD_REQUEST"


# Test cases for PUT /friends/requests/{request_id}
def test_respond_to_request_valid(valid_token, mock_friend_services):
    """
    Test responding to a friend request with valid credentials.
    """
    mock_friend_services.get_request_by_id.return_value = {"recipient_id": "user123"}
    mock_friend_services.update_friend_request_status.return_value = 1

    headers = {"Authorization": f"Bearer {valid_token}"}
    response = client.put("/friends/requests/request123", json={"status": "accepted"}, headers=headers)

    assert response.status_code == 200
    assert response.json() == {"message": "Request status updated successfully: accepted"}

@pytest.mark.parametrize(
    "request_data, payload, expected_status, expected_response",
    [
        ({"recipient_id": "user456"}, {"status": "accepted"}, 403, {"detail": {"code": "PERMISSION_DENIED"}}),  # Not the recipient
        (None, {"status": "accepted"}, 404, {"detail": {"code": "NOT_FOUND"}}),  # Request not found
        ({"recipient_id": "user123"}, {"status": "invalid_status"}, 422, {"detail": [{"msg": "Invalid status value"}]}),  # Invalid status
    ],
)
def test_respond_to_request_edge_cases(valid_token, mock_friend_services, request_data, payload, expected_status, expected_response):
    """
    Test edge cases for responding to a friend request.
    """
    mock_friend_services.get_request_by_id.return_value = request_data

    headers = {"Authorization": f"Bearer {valid_token}"}
    response = client.put("/friends/requests/request123", json=payload, headers=headers)

    assert response.status_code == expected_status
    assert response.json() == expected_response


# Test cases for GET /friends/
def test_get_friends_valid(valid_token, mock_friend_services, mock_user_services):
    """
    Test retrieving the friend list with valid credentials.
    """
    mock_friends = [
        {"user1_id": "user123", "user2_id": "user456", "created_at": "2025-01-01"}
    ]
    mock_user = {"user_id": "user456", "name": "Jane Doe"}
    mock_friend_services.get_friend_list.return_value = mock_friends
    mock_user_services.get_user_by_id.return_value = mock_user

    headers = {"Authorization": f"Bearer {valid_token}"}
    response = client.get("/friends/", headers=headers)

    assert response.status_code == 200
    assert response.json() == [
        {"user_id": "user456", "name": "Jane Doe", "created_at": "2025-01-01"}
    ]

def test_get_friends_unauthorized(invalid_token):
    """
    Test retrieving the friend list with an invalid token.
    """
    headers = {"Authorization": f"Bearer {invalid_token}"}
    response = client.get("/friends/")

    assert response.status_code == 401
    assert response.json()["detail"]["code"] == "UNAUTHORIZED"