from fastapi import FastAPI
import uvicorn
import time
from imageprocessor import *

app = FastAPI()

@app.post("/items/")
def create_item(item: Request):
    print("Processing request. Sleeping for 100")
    results = ProcessRequest(item)
    # Process(target=ProcessRequest, args=(item,))
    # time.sleep(100)
    return item

@app.get("/testconcurrency/")
def concurrency_testing():
    print("Processing request. Sleeping for 30 seconds")
    time.sleep(30)
    print("Finished processing")
    return {"message":"Finished processing"}

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8888)
