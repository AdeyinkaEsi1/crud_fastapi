from pydantic import BaseModel
from pydantic import EmailStr


class UserBase(BaseModel):
   email: EmailStr
class UserCreate(UserBase):
   lname: str
   fname: str
   password: str
