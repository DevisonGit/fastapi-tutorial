from fastapi import FastAPI
from enum import Enum

# criando uma classe enum para validar valores
class ModelName(str, Enum):
    alexnet = 'alexnet'
    resnet = 'resnet'
    lenet = 'lenet'

    
app = FastAPI()

# neste path só é aceito os valores do enum ModelName
@app.get('/models/{model_name}')
async def get_model(model_name: ModelName):
    # comparando pelo valor da classe enumerate
    if model_name is ModelName.alexnet:
        return {'model_name': model_name, 'massege': 'Deep learning FTW'}
    # pegando pelo valor  
    if model_name.value == 'lenet':
        return {'model_name': model_name, 'massege': 'LeCNN all the images'}
    return {'model_name': model_name, 'massege': 'Have some residuals'}
