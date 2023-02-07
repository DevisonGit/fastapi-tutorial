from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse, RedirectResponse

app = FastAPI()

# podemos responder diferente objetos se forem subclasse
@app.get("/portal")
async def get_portal(teleport: bool = False) -> Response:
    if teleport:
        return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    return JSONResponse(content={"message": "Here's your interdimensional portal."})