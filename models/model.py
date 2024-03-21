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
