




# from datetime import timedelta
# from typing import List
# from fastapi.security import OAuth2PasswordRequestForm
# from requests import Session
# from schemas import UserSchema, TodoSchema
# from fastapi import Depends, HTTPException, status
# import app
# from settings import get_current_user, get_db, get_user_todos, update_todo
# from utils.auth import auth_account
# from models.model import TODO, User

# @app.post("/api/users", response_model=UserSchema)
# def signup(user_data: UserSchema.UserCreate, db: Session = Depends(get_db)):
#    """add new user"""
#    user = get_user_by_email(db, user_data.email)
#    if user:
#       raise HTTPException(status_code=409,
#    	                    detail="Email already registered.")
#    signedup_user = create_user(db, user_data)
#    return signedup_user


# @app.post("/api/token", response_model=auth_account)
# def login_for_access_token(db: Session = Depends(get_db),
#                       	form_data: OAuth2PasswordRequestForm = Depends()):
#    """generate access token for valid credentials"""
#    user = auth_account.authenticate_user(db, form_data.username, form_data.password)
#    if not user:
#       raise HTTPException(
#        	status_code=status.HTTP_401_UNAUTHORIZED,
#        	detail="Incorrect email or password",
#        	headers={"WWW-Authenticate": "Bearer"},
#    	)
#    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#    access_token = auth_account.create_access_token(data={"sub": user.email},
#                                   	expires_delta=access_token_expires)
#    return {"access_token": access_token, "token_type": "bearer"}
