from fastapi import FastAPI

app = FastAPI()

@app.get('/file/{file_path:path}')
async def read_file(file_path: str):
    """
        Se o path receber um paths, tem que ser usado o path conversor {file_path:path} 
        e a chamada tem que ter // no inicio do paths  
    """
    with open(file_path, 'r') as file:
        text_file = file.readline()
    return {'file_path': file_path, 'text': text_file}