from pydantic import BaseModel, EmailStr
from datetime import datetime


class UserBase(BaseModel):
    email: EmailStr
    password: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int


class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    # class Config:
    #     from_attributes = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str
