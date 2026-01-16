from fastapi import APIRouter
from schemas.student import StudentCreate

router = APIRouter()

@router.post("/create")
def create_student(student: StudentCreate):
    return {
        "message": "Student profile created",
        "student": student
    }
