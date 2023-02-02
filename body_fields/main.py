from typing import Union
from fastapi import FastAPI, Body
from pydantic import BaseModel, Field

app = FastAPI()

# validando no model
class Item(BaseModel):
    name: str
    description: Union[str, None] = Field(
        default=None, title="the description must be greater than zero", max_length=300
    )
    price: float = Field(gt=0, description="the price must be greater than zero")
    tax: Union[float, None] = None
   
 
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item = Body(embed=True)):
    results = {"item_id": item_id, "item": item}
    return results