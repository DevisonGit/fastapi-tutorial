from typing import List, Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: List[str] = []


@app.post("/items/")
# definindo o tipo de retorno
async def create_item(item: Item) -> Item:
    return item


@app.get("/items/")
async def read_item() -> List[Item]:
    return [
        Item(name="portal gun", price=42.0),
        Item(name="plumbus", price=32.0)
    ]
