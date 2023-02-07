from typing import Union, Any
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

# para cadastrarmos o usuario temos o campo password
class UserIn(BaseModel):
    name: str
    password: str
    email: EmailStr
    full_name: Union[str, None] = None


# para retornamos podemos definir outra response
class UserOut(BaseModel):
    name: str
    email: EmailStr
    full_name: Union[str, None] = None


@app.post("/user/", response_model=UserOut)
async def create_user(user: UserIn) -> Any:
    return user
