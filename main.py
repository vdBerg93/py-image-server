from fastapi import FastAPI
import uvicorn
import time
from imageprocessor import *

app = FastAPI()

@app.post("/items/")
def create_request(item: Request):
    ProcessRequest(item)
    return item

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8888)
