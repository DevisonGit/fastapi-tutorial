from fastapi import FastAPI, HTTPException

app = FastAPI()

items = {"foo": "the foo wrestlers"}


@app.get("/items/{item_id}")
async def read_item(item_id: str):
    # retornando HTTP response com erros
    if item_id not in items:
        raise HTTPException(status_code=404, detail="item not found")
    return {"item": items[item_id]}


@app.get("/items-header/{item_id}")
async def read_item(item_id: str):
    # retornando HTTP response com header costomizado
    if item_id not in items:
        raise HTTPException(status_code=404, detail="item not found", headers={
                            "X-Error": "There goes my error"})
    return {"item": items[item_id]}
