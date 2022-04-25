# Python
from datetime import date
from typing import Optional
from uuid import UUID
#  Pydantic
from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field

class UserBase(BaseModel):
    user_id: UUID= Field(...)
    email: EmailStr= Field(...)
    class Config:
        orm_mode = True

class UserLogin(UserBase):
    password: str = Field(
        ...,
        min_length=8,
        max_length=64
        )

class User(UserBase):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50
        )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50
        )
    birth_date: Optional[date]= Field(default=None)

class LoginOut(BaseModel): 
    email: EmailStr = Field(...)
    message: str = Field(default="Login Succesfully!")
    
class UserRegister(User):
    password: str = Field(
        ...,
        min_length=8,
        max_length=64
     )
