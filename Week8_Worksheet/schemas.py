# schemas.py
from pydantic import BaseModel, EmailStr # type: ignore
from typing import Optional, List

# Shared course properties
class CourseBase(BaseModel):
    title: str
    description: Optional[str] = None
    credits: int = 0

class CourseCreate(CourseBase):
    pass

class CourseRead(CourseBase):
    id: int
    class Config:
        orm_mode = True

# Student schemas
class StudentBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    age: Optional[int] = None

class StudentCreate(StudentBase):
    pass

class StudentRead(StudentBase):
    id: int
    courses: List[CourseRead] = []
    class Config:
        orm_mode = True
