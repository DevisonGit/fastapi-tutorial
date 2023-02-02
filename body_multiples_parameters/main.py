from typing import Union
from fastapi import FastAPI, Path, Body
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


class User(BaseModel):
    username: str
    full_name: Union[str, None] = None


@app.put("/items/{item_id}")
# misturando path, query e body parameters
async def update_item(
    *,
    item_id: int = Path(title="the id of item to get", ge=0, le=1000),
    q: Union[str, None] = None,
    item: Union[Item, None] = None
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    return results


@app.put("/items/multi/{item_id}")
# recebendo multiplos body parameters
async def update_multi(item_id: int, item: Item, user: User):
    result = {"item_id": item_id, "item": item, "user": user}
    return result


@app.put("/items/singular/{item_id}")
# informa um campo para vir no body não no query parameters que é o padrão do fastapi
async def update_multi(item_id: int, item: Item, user: User, importance: int = Body()):
    result = {"item_id": item_id, "item": item,
              "user": user, "importance": importance}
    return result


@app.put("/items/multiple/{item_id}")
# usando multiplos body parameters e query
async def update_multi(
        *,
        item_id: int,
        item: Item,
        user: User,
        importance: int = Body(gt=0),
        q: Union[str, None] = None
):
    results = {"item_id": item_id, "item": item,
              "user": user, "importance": importance}
    if q: 
        results.update({"q": q})
    return results

@app.put("/items/embed/{item_id}")
# o fastapi espera o body direto com esse parametro leva em consideração o nome no json
async def update_multi(item_id: int, item: Item = Body(embed=True)):
    result = {"item_id": item_id, "item": item}
    return result