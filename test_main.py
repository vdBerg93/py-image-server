from fastapi.testclient import TestClient
from main import app
import os
import shutil

client = TestClient(app)

# Test 1: Try doing all operations
def test_create_request_1():
    inputPath = "testimages"
    outputPath = os.path.join("testoutput","test1")
    test_json = {
      "images":[{"input":os.path.join(inputPath,"cyclo1.jpg"),"output":os.path.join(outputPath,"cyclo1_processed.jpg")},
                {"input":os.path.join(inputPath,"cyclo2.jpg"),"output":os.path.join(outputPath,"cyclo2_processed.PNG")},
                {"input":os.path.join(inputPath,"cyclo3.jpg"),"output":os.path.join(outputPath,"cyclo3_processed.jpg")},
                {"input":os.path.join(inputPath,"cyclo4.jpg"),"output":os.path.join(outputPath,"cyclo4_processed.PNG")}],
      "operations": ["splitQuadrants=True","resize=1.5","blur=25"]
    }
    response = client.post(
        "/items/",
        json=test_json,
    )
    assert response.status_code == 200
    assert response.json() == test_json

#Test 2: splitting the images and scaling to original size
def test_create_request_2():
    inputPath = "testimages"
    outputPath = os.path.join("testoutput","test2")
    test_json = {
      "images":[{"input":os.path.join(inputPath,"cyclo1.jpg"),"output":os.path.join(outputPath,"cyclo1_processed.jpg")},
                {"input":os.path.join(inputPath,"cyclo2.jpg"),"output":os.path.join(outputPath,"cyclo2_processed.PNG")},
                {"input":os.path.join(inputPath,"cyclo3.jpg"),"output":os.path.join(outputPath,"cyclo3_processed.jpg")},
                {"input":os.path.join(inputPath,"cyclo4.jpg"),"output":os.path.join(outputPath,"cyclo4_processed.PNG")}],
      "operations": ["splitQuadrants=True","resize=2","splitQuadrants=True","resize=2"]
    }
    response = client.post(
        "/items/",
        json=test_json,
    )
    assert response.status_code == 200
    assert response.json() == test_json

#Test 3: testing edge cases where user provides wrong inputs
def test_create_request_wronginputs():
    inputPath = "testimages"
    outputPath = os.path.join("testoutput","test3")
    test_json = {
      "images":[{"input":os.path.join(inputPath,"cyclo1.jpg"),"output":os.path.join(outputPath,"cyclo1_processed.jpg")},
                {"input":os.path.join(inputPath,"cyclo2.jpg"),"output":os.path.join(outputPath,"cyclo2_processed.PNG")},
                {"input":os.path.join(inputPath,"cyclo3.jpg"),"output":os.path.join(outputPath,"cyclo3_processed.jpg")},
                {"input":os.path.join(inputPath,"cyclo4.jpg"),"output":os.path.join(outputPath,"cyclo4_processed.PNG")}],
      "operations": ["blur=-2","resize=-0.5","splitQuadrants=False","resize=0"]
    }
    response = client.post(
        "/items/",
        json=test_json,
    )
    assert response.status_code == 200
    assert response.json() == test_json

#Test 4: testing edge cases where user provides wrong inputs
def test_create_request_nonexistingfolder():
    inputPath = "testimages"
    outputPath = os.path.join("testoutput","nonexistingfolder")
    try:
        shutil.rmtree(outputPath)
    except:
        print("Folder doesnt exist")

    test_json = {
      "images":[{"input":os.path.join(inputPath,"cyclo1.jpg"),"output":os.path.join(outputPath,"cyclo1_processed.jpg")},
                {"input":os.path.join(inputPath,"cyclo2.jpg"),"output":os.path.join(outputPath,"cyclo2_processed.PNG")},
                {"input":os.path.join(inputPath,"cyclo3.jpg"),"output":os.path.join(outputPath,"cyclo3_processed.jpg")},
                {"input":os.path.join(inputPath,"cyclo4.jpg"),"output":os.path.join(outputPath,"cyclo4_processed.PNG")}],
      "operations": ["blur=0","resize=2","splitQuadrants=False","resize=0"]
    }
    response = client.post(
        "/items/",
        json=test_json,
    )
    assert response.status_code == 200
    assert response.json() == test_json

def test_create_request_nonexistingfile():
    inputPath = "testimages"
    outputPath = os.path.join("testoutput","nonexistingfolder")
    try:
        shutil.rmtree(outputPath)
    except:
        print("Folder doesnt exist")

    test_json = {
      "images":[{"input":os.path.join(inputPath,"thisdoesntexist.jpg"),"output":os.path.join(outputPath,"cyclo1_processed.jpg")},
                {"input":os.path.join(inputPath,"thisdoesntexist.jpg"),"output":os.path.join(outputPath,"cyclo2_processed.PNG")},
                {"input":os.path.join(inputPath,"thisdoesntexist.jpg"),"output":os.path.join(outputPath,"cyclo3_processed.jpg")},
                {"input":os.path.join(inputPath,"thisdoesntexist.jpg"),"output":os.path.join(outputPath,"cyclo4_processed.PNG")}],
      "operations": ["blur=0","resize=2","splitQuadrants=False","resize=0"]
    }
    response = client.post(
        "/items/",
        json=test_json,
    )
    assert response.status_code == 200
    assert response.json() == test_json
