from typing import Dict
from fastapi import FastAPI

app = FastAPI()

@app.post("/index-weights/")
# o body é um dict
async def create_multiple_images(weights: Dict[int, float]):
    return weights
