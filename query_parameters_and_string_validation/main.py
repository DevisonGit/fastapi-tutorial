from typing import Union, List
from fastapi import FastAPI, Query
from pydantic import Required

app = FastAPI()

# podemos usar a Query pra fazer validaçoes, neste caso definindo tamanho maximo
@app.get("/items/max")
async def read_items(q: Union[str, None] = Query(
    default=None, max_length=50
)):
    results = {'items': [{"item": "foo"}, {"item": "bar"}]}
    if q:
        results.update({'q': q})
    return results

# neste caso definindo tamanho minimo maximo
@app.get("/items/min")
async def read_items(q: Union[str, None] = Query(
    default=None, min_length=3
)):
    results = {'items': [{"item": "foo"}, {"item": "bar"}]}
    if q:
        results.update({'q': q})
    return results

# neste caso definindo um regex
@app.get("/items/regex")
async def read_items(q: Union[str, None] = Query(
    default=None, regex='^fixedquery$'
)):
    results = {'items': [{"item": "foo"}, {"item": "bar"}]}
    if q:
        results.update({'q': q})
    return results

# neste caso definindo um valor default
@app.get("/items/default")
async def read_items(q: Union[str, None] = Query(
    default='fixedquery'
)):
    results = {'items': [{"item": "foo"}, {"item": "bar"}]}
    if q:
        results.update({'q': q})
    return results

# para definir um campo obrigatorio basta declara sem o default
@app.get("/items/required")
async def read_items(q: str = Query(
    min_length=3
)):
    results = {'items': [{"item": "foo"}, {"item": "bar"}]}
    if q:
        results.update({'q': q})
    return results

# outra maneira de especificar obrigatoriedade usando reticências (...)
@app.get("/items/required/dot")
async def read_items(q: str = Query(
    default=...
)):
    results = {'items': [{"item": "foo"}, {"item": "bar"}]}
    if q:
        results.update({'q': q})
    return results

# obrigatorio com o None
@app.get("/items/required/none")
async def read_items(q: Union[str, None] = Query(
    default=...
)):
    results = {'items': [{"item": "foo"}, {"item": "bar"}]}
    if q:
        results.update({'q': q})
    return results

# obrigatorio com o Pydentic 
@app.get("/items/required/pydentic")
async def read_items(q: str = Query(
    default=Required
)):
    results = {'items': [{"item": "foo"}, {"item": "bar"}]}
    if q:
        results.update({'q': q})
    return results

# recebendo uma lista de valores
@app.get("/items/list")
async def read_items(q: Union[List[str], None] = Query(default=None)):
    query_items = {"q": q}
    return query_items

# recebendo uma lista de valores com valores default
@app.get("/items/list/default")
async def read_items(q: List[str] = Query(default=['foo', 'bar'])):
    query_items = {"q": q}
    return query_items

# recebendo uma lista sem validaçao
@app.get("/items/list/all")
async def read_items(q: list = Query(default=[])):
    query_items = {"q": q}
    return query_items

# incluindo infomações na hora de incluir a documentação
@app.get("/items/metadata")
async def read_items(
    q: Union[str, None] = Query(
        default=None,
        title="Query string",
        description="Query string for the items to search in the database that have a good match",
        min_length=3,
    )
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# alias no request body ao inves de mandar q mandamos o item-query como campo
@app.get("/items/alias")
async def read_items(q: Union[str, None] = Query(default=None, alias="item-query")):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# para configurar um campo como Deprecating  
@app.get("/items/deprecated")
async def read_items(
    q: Union[str, None] = Query(
        default=None,
        alias="item-query",
        title="Query string",
        description="Query string for the items to search in the database that have a good match",
        min_length=3,
        max_length=50,
        regex="^fixedquery$",
        deprecated=True,
    )
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# esconde o parametro na documentaçao
@app.get("/items/hidden")
async def read_items(
    hidden_query: Union[str, None] = Query(default=None, include_in_schema=False)
):
    if hidden_query:
        return {"hidden_query": hidden_query}
    else:
        return {"hidden_query": "Not found"}