from typing import List, Union, Any
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: List[str] = []


# definindo o tipo de retorno usando o response model
@app.post("/items/", response_model=Item)
async def create_item(item: Item) -> Any:
    return item


@app.get("/items/", response_model=List[Item])
async def read_item() -> Any:
    return [
        Item(name="portal gun", price=42.0),
        Item(name="plumbus", price=32.0)
    ]
