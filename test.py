import pytest
from fastapi.testclient import TestClient
from main import app  # assuming main is the module where your FastAPI app is defined

# Create a TestClient instance
client = TestClient(app)


# Define tests
def test_read_root():
    # Make a GET request to the /test endpoint
    response = client.get("/test")
    
    # Assert that the status code is 200 OK
    assert response.status_code == 200
    
    # Assert that the response body contains the expected data
    assert response.json() == {"Hello": "World"}
