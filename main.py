from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

todos = []

class Todo(BaseModel):
    id: int
    title: str
    completed: bool

@app.post("/todos")
def create_todos(todo:Todo):
    todos.append(todo)
    return {"message": "Todo created successfully", "todo": todo}

@app.get("/todos")
def get_todos():
    return {"todos": todos}

@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return {"todo": todo}
    return {"message": "Todo not found"}

@app.put("/todos/{todo_id}")
def update_todo(todo_id: int ,update_todo: Todo):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos[index] = update_todo
            return {"message": "Todo updated successfully", "todo": update_todo}
    return {"message": "Todo not found"}