from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="TODO Application")


# -----------------------------
# Data Models
# -----------------------------

class TodoCreate(BaseModel):
    task: str


class TodoUpdate(BaseModel):
    task: str
    completed: bool


# -----------------------------
# Temporary Database
# -----------------------------

todos = [
    {
        "id": 1,
        "task": "Learn Docker",
        "completed": False
    },
    {
        "id": 2,
        "task": "Learn Kubernetes",
        "completed": False
    }
]


# -----------------------------
# Home
# -----------------------------

@app.get("/")
def home():
    return {
        "message": "TODO Application is running"
    }


# -----------------------------
# GET ALL TODOS
# -----------------------------

@app.get("/todos")
def get_todos():
    return todos


# -----------------------------
# GET TODO BY ID
# -----------------------------

@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):

    for todo in todos:
        if todo["id"] == todo_id:
            return todo

    raise HTTPException(
        status_code=404,
        detail="TODO not found"
    )


# -----------------------------
# CREATE TODO
# -----------------------------

@app.post("/todos")
def create_todo(todo: TodoCreate):

    new_todo = {
        "id": len(todos) + 1,
        "task": todo.task,
        "completed": False
    }

    todos.append(new_todo)

    return new_todo


# -----------------------------
# UPDATE TODO
# -----------------------------

@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, todo_update: TodoUpdate):

    for todo in todos:

        if todo["id"] == todo_id:

            todo["task"] = todo_update.task
            todo["completed"] = todo_update.completed

            return todo

    raise HTTPException(
        status_code=404,
        detail="TODO not found"
    )


# -----------------------------
# DELETE TODO
# -----------------------------

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):

    for todo in todos:

        if todo["id"] == todo_id:

            todos.remove(todo)

            return {
                "message": "TODO deleted successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="TODO not found"
    )