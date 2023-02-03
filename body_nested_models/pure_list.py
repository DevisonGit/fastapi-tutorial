from typing import List
from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()

class Image(BaseModel):
    url: HttpUrl
    name: str

@app.post("/images/multiple/")
# o body é um lista
async def create_multiple_images(images: List[Image]):
    for imagem in images:
        print(imagem.url)
    return images
