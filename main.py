from fastapi import FastAPI,status,HTTPException,Request
from fastapi.responses import JSONResponse

app = FastAPI()

class Usernotfound(Exception):
    def __init__(self, name: str):
        self.name = name

@app.exception_handler(Usernotfound)
def user_not_found_exception_handler(request: Request, exc: Usernotfound):
            return JSONResponse(
                status_code=404,
                content={"status":"error","message":f"User not found {exc.name}"})

@app.get("/user/{name}")
def get_user(name: str):
    if name !="Aman":
        raise Usernotfound(name)
    return {"name": name}


    
# @app.get("/users/{user_id}")
# def get_user(user_id: int):
#     if user_id != 1:
#         raise HTTPException(status_code=404, detail="Invalid user ID")
#     return {"user_id": 1, "name": "John Doe"}