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

# declarando parametro no path, esse parametro é passado para a função.  
@app.get('/items/{item_id}')
async def read_item(item_id):
    return {'item_id': item_id}

# podemos declarar o tipo de paramentro, se passado outro tipo gera um erro
@app.get('/items/type/{item_id}')
async def read_item_type(item_id: int):
    return {'item_id': item_id}

# a ordem importa se houver dois path que remetam a diferentes funçoes
# a primeira encontrada sera executada
@app.get('/users')
async def read_users():
    return ['Rick', 'Morty']

@app.get('/users')
async def read_users2():
    return ['Bean', 'Elfo']