from typing import Union
from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


@app. put("/items/{item_id}")
# descreve como o body da request deve ser usando o Body do fastAPI
async def update_item(item_id: int, item: Item = Body(example={
    "name": "Foo",
    "description": "A very nice Item with Body",
    "price": 35.4,
    "tax": 3.2
})):
    results = {"item_id": item_id, "item": item}
    return results
