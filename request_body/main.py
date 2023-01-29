from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    """
        Quando queremos enviar dados usamos o request body, aqui declaramos o request body como
        Pydantic, que é um validador e gerenciador de tipos para o python
    """
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    
app = FastAPI()

@app.post("/items/")
async def create_item(item: Item):
    return item
