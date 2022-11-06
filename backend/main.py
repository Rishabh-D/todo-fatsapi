from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from model import Todo
from database import (
  fetch_one_todo, 
  fetch_all_todos, 
  update_todo_data, 
  create_todo, 
  remove_todo
  )

app = FastAPI()

origins = ['http://localhost:3000']
app.add_middleware(
  CORSMiddleware,
  allow_origins = origins,
  allow_credentials = True,
  allow_methods = ["*"],
  allow_headers = ["*"]
)

@app.get("/")
def read_root():
  return {"ping": "pong"}

@app.get("/api/todo")
def get_todo():
  response = fetch_all_todos()
  return response

@app.get("/api/todo/{title}", response_model=Todo)
def get_todo_by_title(title : str):
  response = fetch_one_todo(title)
  if response:
    return response
  raise HTTPException(404, f"no todo item with title: {title} found")

@app.post("/api/todo", response_model=Todo)
def post_todo(todo: Todo):
  response = create_todo(todo.dict())
  if response:
    return response
  raise HTTPException(400, "Bad Request")
  

@app.put("/api/todo/{title}", response_model=Todo)
def update_todo(title : str, desc: str):
  print("in main app.put")
  response = update_todo_data(title, desc)
  print("response generated", response)
  if response:
    return response
  raise HTTPException(404, 404, f"no todo item with title: {title} found")
  

@app.delete("/api/todo/{title}")
def delete_todo(title : str):
  response = remove_todo(title)
  if response:
    return "successfully deleted"
  raise HTTPException(404, 404, f"no todo item with title: {title} found")
  
  