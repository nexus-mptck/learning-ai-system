from pydantic import BaseModel

class StudentCreate(BaseModel):
    nickname: str
    age: int
    grade: str
