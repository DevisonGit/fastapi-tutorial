from typing import List, Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: float = 10.5
    tags: List[str] = []

items = {
    "foo": {"name": "foo", "price": 50.2},
    "bar": {"name": "bar", "description": "the bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []}
}

# omitindo campos não preenchidos do model
@app.get("/items/", response_model=Item, response_model_exclude_unset=True)
async def read_item(item_id: str):
    return items[item_id]
