import pytest
from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)

# Fixtures for reusable test data
@pytest.fixture
def valid_user_signup():
    """
    Fixture for a valid user signup data.

    Return:
        Dictionary with valid user details.
    """
    return {
        "name": "Ahmed Chukwudi",
        "email": "ahmedchukwudi@email.com",
        "password": "securepassword0101",
    }

@pytest.fixture
def existing_user_signup():
    """
    Fixture for existing user signup data.
    Simulates a scenario where the email is already registered.
    """
    return {
        "name": "Ifeanyi Bayode",
        "email": "ifeanyibayode@email.com",
        "password": "securepassword0101",
    }

@pytest.fixture
def valid_user_login():
    """
    Fixture for valid user login data.

    Return:
        Dictionary with correct email and password.
    """
    return {
        "email": "ahmedchukwudi@email.com",
        "password": "securepassword0101",
    }

@pytest.fixture
def invalid_user_login():
    """
    Fixture for invalid user login data.
    Simulates incorrect email or password for login.
    """
    return {
        "email": "invaliduser@email.com",
        "password": "wrongpassword123",
    }

# Test cases
def test_signup_success(valid_user_signup, monkeypatch):
    """
    Tests success scenario for the signup endpoint. 
    This verifies that the API returns a success message and user ID
    when valid user details are provided.
    """
    # Mock class to simulate returned user object
    class MockUser:
        def __init__(self, user_id):
            self.user_id = user_id

    async def mock_create_user(self, signup):
        return MockUser(user_id="user123")
    
    monkeypatch.setattr(
        "app.services.auth_service.AuthService.create_user", mock_create_user
    )

    response = client.post("/auth/signup", json=valid_user_signup)
    assert response.status_code == 201
    assert response.json() == {
        "message": "User registered successfully",
        "user": "user123",
    }
    
def test_signup_existing_user(existing_user_signup, monkeypatch):
    """
    Test failure scenario for the login endpoint when incorrect credentials are
    provided. This verifies that the API returns a 401 error with an appropriate
    message.
    """
    async def mock_create_user(self, signup):
        raise ValueError("User already exists")

    monkeypatch.setattr(
        "app.services.auth_service.AuthService.authenticate_user", mock_create_user)
    
    # Mock database dependency
    async def mock_get_db():
        class MockDatabase:
            async def insert_user(self, user):
                raise ValueError("User already exists")

            async def find_user_email(self, email):
                return {"email": email, "name": "Existing User"}
            
        return MockDatabase()
    
    app.dependency_overrides[get_db] = mock_get_db

    response = client.post("/auth/signup", json=existing_user_signup)
    assert response.status_code == 400
    assert "detail" in response.json()
    assert response.json()["detail"]["error"] == "User already exists"

@pytest.mark.parametrize(
    "signup_data",
    [
        {}, # Empty payload
        {"name": "Ngozi Usman"},  # Missing email and password
        {"email": "ngoziusman@email.com"},  # Missing name and password
    ],
)
def test_signup_missing_fields(signup_data):
    """
    Tests signup with incomplete or missing data. This ensures the API returns
    a 422 Unprocessable Entity error.
    """
    response = client.post("/auth/signup", json=signup_data)
    assert response.status_code == 422
    assert "detail" in response.json()

@pytest.mark.parametrize(
    "login_data, expected_status, expected_response",
    [
        (
            {"email": "ngoziusman@email.com", "password": "securepassword123"},
            200,
            {"access_token": "mocktoken123", "token_type": "bearer"},
        ),
        (
            {"email": "invaliduser@email.com", "password": "wrongpassword121"},
            401,
            {"detail": {"code": "UNAUTHORIZED", "error": "Invalid email or password"}},
        ),
    ],
)
def test_login_cases(login_data, expected_status, expected_response, monkeypatch):
    """
    Tests login functionality for both valid and invalid credentials.
    Mocks the `authenticate_user` service to return success or None based on the input
    """
    async def mock_authenticate_user(self, email, password):
        if email == "ngoziusman@email.com" and password == "securepassword123":
            return {"access_token": "mocktoken123", "token_type": "bearer"}
        return None
    
    monkeypatch.setattr(
        "app.services.auth_service.AuthService.authenticate_user",
        mock_authenticate_user,
    )

    response = client.post("/auth/login", json=login_data)
    assert response.status_code == expected_status
    assert response.json() == expected_response

@pytest.mark.parametrize(
    "login_data",
    [
        {},  # Empty payload
        {"email": "ngoziusman@email.com"},  # Missing password
        {"password": "securepassword123"},  # Missing email
    ],
)
def test_login_missing_fields(login_data):
    """
    Tests login with incomplete or mising data. This ensures the API returns
    a 422 Unprocessable Entity error.
    """
    response = client.post("/auth/login", json=login_data)
    assert response.status_code == 422
    assert "detail" in response.json()
    
def test_signup_invalid_email_format(valid_user_signup):
    """
    Tests signup with an invalid email format. This ensures the API returns a 422
    Unprocessable Entity error.
    """
    valid_user_signup["email"] = "invalidemail"
    response = client.post("/auth/signup", json=valid_user_signup)
    assert response.status_code == 422
    assert "detail" in response.json()

# def test_login_success(valid_user_login, monkeypatch):
#     """
#     Test success scenario for the login endpoint.
#     This verifies that the API returns a valid access token when correct
#     credentials are provided.
#     """
#     async def mock_authenticate_user(email, password):
#         return {
#             "access_token": "mocktoken123",
#             "token_type": "bearer",
#         }

#     monkeypatch.setattr(
#         "app.services.auth_service.AuthService.authenticate",
#         mock_authenticate_user,
#     )

#     response = client.post("/suth/login", json=valid_user_login)
#     assert response.status_code == 200
#     assert response.json() == {
#         "access_token": "mocktoken123",
#         "token_type": "bearer",
#     }

# def test_login_invalid_user(invalid_user_login, monkeypatch):
#     """
#     Test a failure scenario for the login endpoint when incorrect credentials
#     are provided. This verifies that the API returns a 401 error with an appropriate
#     message.
#     /"""
#     async def mock_authenticate_user(email, password):
#         return None
    
#     monkeypatch.setattr(
#         "app.services.auth_service.AuthService.authenticate_user",
#         mock_authenticate_user,
#     )

#     response = client.post("/auth/login", json=invalid_user_login)
#     assert response.status_code == 401
#     assert response.json()["detail"]["error"] == "Invalid email or password"