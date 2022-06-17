from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_item():
    test_json = {
      "inputs": [],
      "outputs": [],
      "operations": []
    }
    response = client.post(
        "/items/",
        json=test_json,
    )
    assert response.status_code == 200
    assert response.json() == test_json
