from datetime import timedelta
from typing import List
from requests import Session
from schemas import UserSchema, TodoSchema
from fastapi import Depends, HTTPException, status
import app
from settings import get_current_user, get_db, get_user_todos, update_todo
from utils.auth import auth_account
from models.model import TODO, User


@app.get("/api/mytodos", response_model=List[TODO])
def get_own_todos(current_user: User = Depends(get_current_user),
             	db: Session = Depends(get_db)):
   """return a list of TODOs owned by current user"""
   todos = get_user_todos(db, current_user.id)
   return todos


@app.post("/api/todos", response_model=TODO)
def add_a_todo(todo_data: schemas.TODOCreate,
          	current_user: models.User = Depends(get_current_user),
          	db: Session = Depends(get_db)):
   """add a TODO"""
   todo = create_meal(db, current_user, meal_data)
   return todo


@app.put("/api/todos/{todo_id}", response_model=TODO)
def update_a_todo(todo_id: int,
             	todo_data: TodoSchema.TODOUpdate,
             	current_user: User = Depends(get_current_user),
             	db: Session = Depends(get_db)):
   """update and return TODO for given id"""
   todo = get_user_todos(db, todo_id)
   updated_todo = update_todo(db, todo_id, todo_data)
   return updated_todo


@app.delete("/api/todos/{todo_id}")
def delete_a_meal(todo_id: int,
             	current_user: User = Depends(get_current_user),
             	db: Session = Depends(get_db)):
   """delete TODO of given id"""
   delete_meal(db, todo_id)
   return {"detail": "TODO Deleted"}