# importar o FastAPI
from fastapi import FastAPI

# instanciar a class FastAPI, sera o ponto de interaçao para criar todo o app
app = FastAPI()

# cria o decorator path da operaçao, informando o caminho e o metodo.
# metodos = [POST, GET, PUT, DELETE, OPTIONS, HEAD, PATCH, TRACE] 
@app.get('/')
# um função normal do python
async def root():
    # retorno da função
    return {'message': 'hello world'}
