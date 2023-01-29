from fastapi import FastAPI
from typing import Union

app = FastAPI()

fake_items_db = [
    {'item': 'foo'},
    {'item': 'bar'},
    {'item': 'baz'}
]

# quando declaramos varios parametros automaticamente eles viram 'query' 
# na url eles começam depois da ? e são separados por & exemplo: /items/?skip=0&limit=10
@app.get('/items/')
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]

# podemos declarar parametros opcionais 
@app.get('/items/{item_id}/')
async def read_item_optional(item_id: str, q: Union[str, None] = None):
    if q:
        return {'item': item_id, 'q': q}
    return {'item_id': item_id}

# para declarar parametros obrigatorios, basta declarar sem o valor default 
@app.get('/items/required/{item_id}/')
async def read_item_required(item_id: str, needy: str):
    return {'item_id': item_id, 'needy': needy}

# podemos combinar todos os tipos
@app.get('/items/all/{item_id}/')
async def read_item_required(item_id: str, needy: str, skip: int = 0, limit: Union[int, None] = None):
    return {'item_id': item_id, 'needy': needy, 'skip': skip, 'limit': limit}
