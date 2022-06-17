from fastapi.testclient import TestClient
from main import app
import multiprocessing

client = TestClient(app)

def test_create_item():
    inputPath = "testimages"
    outputPath = "testoutput"
    test_json = {
      "images":[{"input":inputPath+"/cyclo01.jpg","output":outputPath+"/cycl01_processed.jpg"},
                {"input":inputPath+"/cyclo02.jpg","output":outputPath+"/cycl02_processed.jpg"},
                {"input":inputPath+"/cyclo03.jpg","output":outputPath+"/cycl03_processed.jpg"},
                {"input":inputPath+"/cyclo04.jpg","output":outputPath+"/cycl04_processed.jpg"}],
      "operations": ["operation1","operation2"]
    }
    response = client.post(
        "/items/",
        json=test_json,
    )
    assert response.status_code == 200
    assert response.json() == test_json
{
  "images": [],
  "operations": [
    "string"
  ]
}
