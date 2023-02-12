from fastapi import FastAPI, File, UploadFile

app = FastAPI()


@app.post("/files/")
async def create_file(file: bytes = File(description='A file read as bytes')):
    # com metadata
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(description="A file read as uploadFile")):
    # com metadata
    return {"filename": file.filename}
