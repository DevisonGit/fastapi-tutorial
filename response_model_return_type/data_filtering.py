from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class BaseUser(BaseModel):
    name: str
    email: EmailStr
    full_name: Union[str, None] = None


class UserIn(BaseUser):
    password: str

# podemos fazer o return atraves de herança
@app.post("/user/")
async def create_user(user: UserIn) -> BaseUser:
    return user
