from typing import Union
from fastapi import Cookie, FastAPI


app = FastAPI()

@app.get("/items/")
# podemos coletar informações de cookie
async def read_items(asd_id: Union[str,None] = Cookie(default=None)):
    return {"asd_id": asd_id + " ok"}
