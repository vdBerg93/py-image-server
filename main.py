from fastapi import FastAPI
import uvicorn
import time
from imageprocessor import *

app = FastAPI()

@app.post("/items/")
def create_request(item: Request):
    ProcessRequest(item)
    return item

@app.get("/")
def root():
    return {"header":"This is the root of the HTTP image processing server",
            "option 1":"Try a test message through http://localhost:8888/docs#/default/create_request_items__post",
            "option 2":"Run several processing tests by running test_main.py from console or through your IDE"}

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8888)
