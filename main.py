from fastapi import FastAPI
from routes import student, analyze
from database.db import engine
from database.models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Learning Difficulty Detection API",
    description="AI-based behavioral learning risk analysis",
    version="1.0"
)

app.include_router(student.router, prefix="/student", tags=["Student"])
app.include_router(analyze.router, prefix="/analyze", tags=["AI Analysis"])

@app.get("/")
def home():
    return {"status": "Backend running successfully"}
