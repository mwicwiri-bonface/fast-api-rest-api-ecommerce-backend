from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, StrictStr, EmailStr


class BaseUser(BaseModel):
    username: StrictStr
    email: EmailStr

    class Config:
        orm_mode = True

    def __repr__(self):
        return "<User(id='%s', username='%s', email='%s')>" % (self.id, self.username, self.email)


class User(BaseUser):
    id: int
    full_name: Optional[StrictStr] = None
    is_active: bool = False
    role: Enum
    updated_at: Optional[datetime] = None
    created_at: Optional[datetime] = None


class UserCreate(BaseUser):
    password: StrictStr


class UserUpdate(BaseModel):
    full_name: Optional[StrictStr] = None

    class Config:
        orm_mode = True
