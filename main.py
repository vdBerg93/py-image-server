from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import time
from multiprocessing import Process
from imageprocessor import ProcessRequest, Image

app = FastAPI()

class Item(BaseModel):
    images: List[Image] = []
    operations: List[str] | None = None

# class Item(BaseModel):
#     inputs: List[str] = []
#     outputs: List[str] = []
#     operations: List[str] = []

@app.post("/items/")
def create_item(item: Item):
    print("Processing request. Sleeping for 100")
    results = ProcessRequest(item)
    # Process(target=ProcessRequest, args=(item,))
    # time.sleep(100)
    return item

@app.get("/testconcurrency/")
def test_concurrency():
    print("Processing request. Sleeping for 30 seconds")
    time.sleep(30)
    print("Finished processing")
    return {"message":"Finished processing"}

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8888)
