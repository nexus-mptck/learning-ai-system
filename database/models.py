from sqlalchemy import Column, Integer, String, Float
from database.db import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    nickname = Column(String)
    age = Column(Integer)
    grade = Column(String)

    adhd_risk = Column(String)
    dyslexia_risk = Column(String)
    dyscalculia_risk = Column(String)
