from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: float = 10.5


items = {
    "foo": {"name": "foo", "price": 50.2},
    "bar": {"name": "bar", "description": "the bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "baz", "description": None, "price": 50.2, "tax": 10.5}
}

# especificando o que contera no retorno
@app.get("/items/{item_id}/name", response_model=Item, response_model_include=["name", "description"])
async def read_item(item_id: str):
    return items[item_id]

# excluindo campo do retorno
@app.get("/items/{item_id}/public", response_model=Item, response_model_exclude=["tax"])
async def read_item(item_id: str):
    return items[item_id]