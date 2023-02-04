from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Item(BaseModel):
    # descreve como o body da request deve ser usando field
    name: str = Field(example="Foo")
    description: Union[str, None] = Field(
        default=None, example="A very nice Item with field")
    price: float = Field(example=35.4)
    tax: Union[float, None] = Field(default=None, example=3.2)


@app. put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results
