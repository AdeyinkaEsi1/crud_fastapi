from enum import Enum
from pydantic import BaseModel
from uuid import uuid4, UUID
from typing import List, Optional



class Role(str, Enum):
    admin = "admin"
    user = "user"

class Gender(str, Enum):
    male = "male"
    female = "female"

class User(BaseModel):
    id: Optional[UUID] = uuid4
    first_name: str
    last_name: str
    gender: Gender
    roles: List[Role]

class UpdateUser(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    roles: Optional[List[Role]]




from enum import Enum
from typing import List, Optional
from uuid import UUID, uuid4
from pydantic import BaseModel




    













# import os
# from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, create_engine
# from sqlalchemy.orm import relationship
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# SQLALCHEMY_DATABASE_URL = os.environ['SQLALCHEMY_DATABASE_URL']
# engine = create_engine(
#    SQLALCHEMY_DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()

# class User(Base):
#     __tablename__ = 'users'
#     id = Column(Integer, primary_key=True, index=True)
#     lname = Column(String)
#     fname = Column(String)
    # todos = relationship("TODO", back_populates="owner", cascade="all, delete-orphan")


# class TODO(Base):
#     __tablename__ = 'todos'
#     id = Column(Integer, primary_key=True, index=True)
#     text = Column(String, index=True)
#     completed = Column(Boolean, default=False)
#     owner_id = Column(Integer, ForeignKey('users.id'))
#     owner = relationship("User", back_populates="todos")
