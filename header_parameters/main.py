from typing import Union, List
from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/items/")
# podemos coletar informações do header da request
async def read_items(user_agent: Union[str, None] = Header(default=None)):
    return {"User-agent": user_agent}


@app.get("/items/under/")
# o Header do fastAPI converte (-) em (_) podemos desabilitar
async def read_items(strange_header: Union[str, None] = Header(default=None, convert_underscores=False)):
    return {"strange_header": strange_header}


@app.get("/items/duplicate/")
# se recebermos header duplicado, podemos usa um lista para capturar os valores
async def read_items(x_token: Union[List[str], None] = Header(default=None)):
    return {"X-Token values": x_token}
