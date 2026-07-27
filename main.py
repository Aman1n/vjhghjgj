from fastapi import FastAPI,status,HTTPException


app = FastAPI()

@app.post("/create", status_code=status.HTTP_201_CREATED)
def create_item():
    return {"message": "Item created successfully"}

@app.get("/user")
def get_users():
    return{
        "status": "success",
        "message": "User retrieved successfully",
        "data": {
            "id": 1,
            "name": "John Doe",
            "email": "amnaagg2004@"
        }
    }

@app.get("/user/{user_id}")
def get_user(user_id: int):
    if user_id == 1:
        return {
            "status": "success",
            "message": "User retrieved successfully",
            "data": {
                "id": 1,
                "name": "John Doe",
                "email": "amnaagg2004@"
            }
        }
    else:
        raise HTTPException(status_code=404, detail="User not found")