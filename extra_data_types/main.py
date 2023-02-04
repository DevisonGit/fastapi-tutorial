"""
O fastAPI aceita outros tipos alem dos comuns int, float, str, bool, alguns exemplos:
    UUID - id unico universal - representado por uma str
    datetime.datetime - lida com data e hora no python - representado por uma str
    datetime.date - lida com data no python - representado por uma str
    datetime.time - lida com hora no python - representado por uma str
    datetime.timedelta - lida com total de segundos - representado por uma float
    frozenset - set do python - representado por um schema
    bytes - gera um str com o formato binario - respresentado por um str
    decimal - Decimanl do Python - representado por um float
Para mais exemplos verificar documentação do pydantic
"""
from datetime import datetime, time, timedelta
from typing import Union
import uuid
from fastapi import Body, FastAPI
from time import sleep

app = FastAPI()

URL = "https://www.geeksforgeeks.org/fibonacci-sum-subset-elements/"


@app.put("/items/{item_id}")
async def read_items(
    item_id: uuid.UUID,
    start_datetime: Union[datetime, None] = Body(default=None),
    end_datetime: Union[datetime, None] = Body(default=None),
    repeat_at: Union[time, None] = Body(default=None),
    process_after: Union[timedelta, None] = Body(default=None),
):
    start_process = start_datetime + process_after
    duration = end_datetime - start_process
    return {
        "item_id": item_id,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
        "repeat_at": repeat_at,
        "process_after": process_after,
        "start_process": start_process,
        "duration": duration,
    }


@app.get("/items/gerador/")
async def gerar_info():
    start_time = datetime.now()
    item_id = uuid.uuid1()
    sleep(1)
    end_time = datetime.now()
    duration = end_time - start_time
    return {"item_id": item_id, "start_time": start_time, "end_time": end_time, "duration": duration}
