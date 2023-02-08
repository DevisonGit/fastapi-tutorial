from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str
    

items = [
    {"name": "foo", "description": "there comes my hero"},
    {"name": "red", "description": "it's my aeroplane"}
]

@app.get("/items/", response_model=List[Item])
async def read_item():
    return items