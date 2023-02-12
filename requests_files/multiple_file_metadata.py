from fastapi import FastAPI, File, UploadFile
from typing import List
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.post("/files/")
async def create_files(files: List[bytes] = File(description="Multiple files as bytes")):
    # retorna o tamanho dos arquivos enviados na lista
    return {"file_sizes": [len(file) for file in files]}


@app.post("/uploadfiles/")
async def create_upload_file(files: List[UploadFile] = File(description="Multiple files as UploadFile")):
    # retorna o nome dos arquivos enviado na lista
    return {"filenames": [file.filename for file in files]}


@app.get("/")
async def main():
    # gera um conteudo html que permite envio de arquivos e recebe a chamada
    content = """
<body>
<form action="/files/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
<form action="/uploadfiles/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)
