from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    username: str
    age: int

@app.post("/create-user")
def create_user(user: User):
    """
    Creates a new user. with this api you can create a new user by providing the username and age in the request body. The endpoint will return a success message along with the created user details.
    gukgkhkjhkjhilhikbuk
    hfvjygkugku
    """
    return {'MESSAGE': 'User created successfully', 'user': user}

