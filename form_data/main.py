from fastapi import FastAPI, Form

app = FastAPI()


# podemos receber um formulario
@app.post("/login/")
async def login(username: str = Form(), password: str = Form()):
    return {"username": username}
