from pydantic import Field, BaseModel
from typing import Optional
# 型チェックのための型定義

class Departments(BaseModel):
    id: int
    name: str = Field(min_length=1, maxlength=10)


class Users(BaseModel):
    id: int
    user_name: str = Field(min_length=1, max_length=10)

class UsersInsert(BaseModel):
    id:int
    user_name: str
    departments_id: int
