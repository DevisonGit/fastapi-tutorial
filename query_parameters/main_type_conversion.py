from fastapi import FastAPI
from typing import Union

app = FastAPI()

# podemos declarar parametros boleanos que são convertidos
# True = [1, True, on, yes] 
# False = [0, no, False]
@app.get('/items/{item_id}/')
async def read_item(item_id: str, q: Union[str, None] = None, short: bool = False):
    item = {'item_id': item_id}
    if q:
        item.update({'q': q})
    if not short:
        item.update(
            {'decription':'This is an amazing item has a long description'}                    
        )
    return item

# podemos usar multiplos path e query parametros não precisam esta em ordem são identificados pelo nome
@app.get('/users/{user_id}/items/{item_id}/')
async def read_user_item(item_id: str, user_id: int, q: Union[str, None] = None, short: bool = False):
    item = {'item_id': item_id, 'owner_id': user_id}
    if q:
        item.update({'q': q})
    if not short:
        item.update(
            {'decription':'This is an amazing item has a long description'}                    
        )
    return item