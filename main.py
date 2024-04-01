from typing import List
from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException
from models.model import Gender, Role, User
from models.model import UpdateUser


app = FastAPI()


db: List[User] = [User(
 id=uuid4(),
 first_name="John",
 last_name="ornstein",
 gender=Gender.male,
 roles=[Role.user],
 ),
# ===================================================================================== short test summary info ====================================================================================== 
# ERROR tests/routes/test_presets.py::TestPresets::test_create_and_delete_preset_integration - pymongo.errors.ServerSelectionTimeoutError: 
# SSL handshake failed: ac-ukcsyby-shard-00-00.k7xys16.mongodb.net:27017: _ssl.c:989: 
# The handshake operation timed out,ac-ukcsyby-shard-00-02.k7xys16...
 User(
 id=uuid4(),
 first_name="Jane",
 last_name="manois",
 gender=Gender.female,
 roles=[Role.user],
 ),

 User(
 id=uuid4(),
 first_name="James",
 last_name="Gabriel",
 gender=Gender.male,
 roles=[Role.user],
 ),
 User(
 id=uuid4(),
 first_name="Eunit",
 last_name="Eunit",
 gender=Gender.male,
 roles=[Role.admin, Role.user],
 ),
]


@app.get("/")
async def root():
 return {"Hello": "World",}

@app.get("/api/v1/users", tags=["User"])
async def get_users():
 return db

@app.post("/api/v1/users", tags=["User"])
async def create_user(user: User):
 db.append(user)
 return {"id": user.id}

@app.delete("/api/v1/users/{id}", tags=["User"])
async def delete_user(id: UUID):
  for user in db:
   if user.id == id:
    db.remove(user)
    return {"message": "user deleted"}
   return
  raise HTTPException(
    status_code=404, detail=f"Delete user failed, id {id} not found.")


@app.put("/api/v1/users/{id}", tags=["User"])
async def update_user(user_update: UpdateUser, id: UUID):
 for user in db:
  if user.id == id:
   if user_update.first_name is not None:
    user.first_name = user_update.first_name
   if user_update.last_name is not None:
    user.last_name = user_update.last_name
   if user_update.roleS is not None:
    user.roles = user_update.roles
   return user.id
  raise HTTPException(status_code=404, detail=f"Could not find user with id: {id}")
