from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# class User(BaseModel):
#     username: str
#     age: int
#     email: str

# @app.post("/create-user")
# def create_user(user: User):
#     return {'MESSAGE': 'User created successfully',
#              'user': user}

class address(BaseModel):
    street: str
    city: str
    state: str
    pincode: int

class User(BaseModel):
    username: str
    age: int
    email: str
    address: address

@app.post("/create-user-with-address")
def create_user_with_address(user: User):
    return {'MESSAGE': 'User with address created successfully',
             'user': user}

