from typing import Union
from fastapi import FastAPI, Path, Query

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(item_id: int = Path(title='The id of the item to get'),
                     q: Union[str, None] = Query(default=None, alias='item-query'),):
    results = {"item_id": item_id}
    if q:
        results.update({'q': q})
    return results


# * truque para a query parameters não precisar da um valor default ou da query
@app.get("/items/tricks/{item_id}")
async def read_items(*, item_id: int = Path(title="The ID of the item to get"), q: str):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


# trata valores numericos gt significa > (maior que) ge significa >= (maior igual)
@app.get("/items/gt/{item_id}")
async def read_items(q: str, item_id: int = Path(title="The ID of the item to get", ge=1)):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


# trata valores numericos lt significa < (menor) le significa <= (menor igual)
@app.get("/items/le/{item_id}")
async def read_items(
    *,
    item_id: int = Path(title="The ID of the item to get", gt=0, le=1000),
    q: str,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

# trata valores tipo float
@app.get("/items/float/{item_id}")
async def read_items(
    *,
    item_id: int = Path(title="The ID of the item to get", ge=0, le=1000),
    q: str,
    size: float = Query(ge=0, lt=10.5)
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
