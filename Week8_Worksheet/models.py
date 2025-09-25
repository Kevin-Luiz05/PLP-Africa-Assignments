# models.py
from sqlalchemy import Column, Integer, String, Text, Table, ForeignKey # type: ignore
from sqlalchemy.orm import relationship # type: ignore
from database import Base

# association table for many-to-many (students <-> courses)
enrollments = Table(
    "enrollments",
    Base.metadata,
    Column("student_id", Integer, ForeignKey("students.id"), primary_key=True),
    Column("course_id", Integer, ForeignKey("courses.id"), primary_key=True),
)

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(200), unique=True, index=True, nullable=False)
    age = Column(Integer, nullable=True)

    courses = relationship("Course", secondary=enrollments, back_populates="students")

class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)
    credits = Column(Integer, default=0)

    students = relationship("Student", secondary=enrollments, back_populates="courses")
