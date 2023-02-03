from typing import Set, Union, List
from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()

class Image(BaseModel):
    url: HttpUrl
    name: str
    
class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: Set[str] = set()
    image: Union[List[Image], None] = None

class Offer(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    # usando aninhamento profundo
    items: List[Item]

@app.post("/offers/")
async def create_offer(offer: Offer):
    return offer