from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class Item(BaseModel):
    inputs: List[str] = []
    outputs: List[str] = []
    operations: List[str] = []

@app.post("/items/")
async def create_item(item: Item):
    return item

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8888)
