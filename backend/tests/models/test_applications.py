import pytest
from app.models.applications import ApplicationCreate, ApplicationResponse
from pydantic import ValidationError
from datetime import datetime
from uuid import uuid4


def test_application_create_model():
    """Test ApplicationCreate model with valid and invalid input."""
    # Valid input
    valid_data = {"project_id": "projectxxxx"}
    app_create = ApplicationCreate(**valid_data)
    assert app_create.project_id == "projectxxxx"

    # Invalid input
    invalid_data = {"project_id": None}
    with pytest.raises(ValidationError):
        ApplicationCreate(**invalid_data)


    def test_application_response_model():
        """Test ApplicationResponse model with various input cases."""
        # Valid input
        valid_response_data = {
            "_id": str(uuid4()),
            "project_id": "projectxxxx",
            "applicant_id": str(uuid4()),
            "status": "approved",
            "created_at": datetime.now().isoformat(),
        }
        app_response = ApplicationResponse(**valid_response_data)
        assert app_response.application_id == valid_response_data["_id"]
        assert app_response.project_id == "projectxxxx"
        assert app_response.status == "approved"

        # Test default values
        default_data = {
            "_id": str(uuid4()),
            "project_id": "projectxxxx",
            "applicant_id": str(uuid4()),
        }
        app_response = ApplicationResponse(**default_data)
        assert app_response.status == "pending"
        assert app_response.created_at is not None

        # Invalid status
        invalid_status_data ={
            "_id": str(uuid4()),
            "project_id": "projectxxxx",
            "applicant_id": str(uuid4()),
            "status": "invalid_status",
        }
        with pytest.raises(ValidationError):
            ApplicationResponse(**invalid_status_data)

        # Edge cases
        empty_project_id = {
            "_id": str(uuid4()),
            "project_id": "",
            "applicant_id": str(uuid4()),
        }
        with pytest.raises(ValidationError):
            ApplicationResponse(**empty_project_id)