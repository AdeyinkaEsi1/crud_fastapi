



# from fastapi.security import OAuth2PasswordBearer
# from requests import Session
# import app
# from models.model import SessionLocal, User, TODO
# from fastapi import Depends
# from schemas import UserSchema, TodoSchema
# from utils.auth.auth_account import decode_access_token
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth")


# def get_db():
#    """provide db session to path operation functions"""
#    try:
#     db = SessionLocal()
#     yield db
#    finally:
#    	db.close()
# def get_current_user(db: Session = Depends(get_db),
#                 	token: str = Depends(oauth2_scheme)):
#    return decode_access_token(db, token)


# @app.get("/api/me", response_model=UserSchema)
# def read_logged_in_user(current_user: User = Depends(get_current_user)):
#    """return user settings for current user"""
#    return current_user


# def create_todo(db: Session, current_user: User, todo_data: TodoSchema.TODOCreate):
#    todo = TODO(text=todo_data.text,
#                    	completed=todo_data.completed)
#    todo.owner = current_user
#    db.add(todo)
#    db.commit()
#    db.refresh(todo)
#    return todo


# def update_todo(db: Session, todo_data: TodoSchema.TODOUpdate):
#    todo = db.query(TODO).filter(TODO.id == id).first()
#    todo.text = todo_data.text
#    todo.completed = todo.completed
#    db.commit()
#    db.refresh(todo)
#    return todo


# def delete_todo(db: Session, id: int):
#    todo = db.query(TODO).filter(TODO.id == id).first()
#    db.delete(todo)
#    db.commit()
 

# def get_user_todos(db: Session, userid: int):
#    return db.query(TODO).filter(TODO.owner_id == userid).all()
