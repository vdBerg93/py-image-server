from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_item():
    inputPath = "testimages"
    outputPath = "testoutput"
    test_json = {
      "images":[{"input":inputPath+"/cyclo1.jpg","output":outputPath+"/cyclo1_processed.jpg"},
                {"input":inputPath+"/cyclo2.jpg","output":outputPath+"/cyclo2_processed.jpg"},
                {"input":inputPath+"/cyclo3.jpg","output":outputPath+"/cyclo3_processed.jpg"},
                {"input":inputPath+"/cyclo4.jpg","output":outputPath+"/cyclo4_processed.jpg"}],
      "operations": ["splitQuadrants=True","resize=1.5","blur=25"]
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
