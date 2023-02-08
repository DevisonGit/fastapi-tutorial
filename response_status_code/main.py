from fastapi import FastAPI, status

app = FastAPI()

# podemos configurar o http response
@app.post("/items/", status_code=201)
async def create_item(name: str):
    return {"name": name}

# podemos usar o status do fastAPI para lembrar os codigos HTTP
@app.post("/items/remember/", status_code=status.HTTP_201_CREATED)
async def create_item(name: str):
    return {"name": name}
