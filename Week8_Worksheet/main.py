# main.py
from fastapi import FastAPI, Depends, HTTPException, status # type: ignore
from sqlalchemy.orm import Session                          # type: ignore
import models, schemas
from database import SessionLocal, engine
from typing import List

# create DB tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="PLP Week 8 — Students & Courses CRUD")

# Dependency: get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ---------- Student endpoints ----------
@app.post("/students/", response_model=schemas.StudentRead, status_code=status.HTTP_201_CREATED)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    # avoid duplicate emails
    existing = db.query(models.Student).filter(models.Student.email == student.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    db_student = models.Student(**student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

@app.get("/students/", response_model=List[schemas.StudentRead])
def list_students(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    students = db.query(models.Student).offset(skip).limit(limit).all()
    return students

@app.get("/students/{student_id}", response_model=schemas.StudentRead)
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@app.put("/students/{student_id}", response_model=schemas.StudentRead)
def update_student(student_id: int, payload: schemas.StudentCreate, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    # check email conflict
    if student.email != payload.email:
        other = db.query(models.Student).filter(models.Student.email == payload.email).first()
        if other:
            raise HTTPException(status_code=400, detail="Email already used by another student")
    for field, value in payload.dict().items():
        setattr(student, field, value)
    db.add(student)
    db.commit()
    db.refresh(student)
    return student

@app.delete("/students/{student_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    db.delete(student)
    db.commit()
    return

# ---------- Course endpoints ----------
@app.post("/courses/", response_model=schemas.CourseRead, status_code=status.HTTP_201_CREATED)
def create_course(course: schemas.CourseCreate, db: Session = Depends(get_db)):
    db_course = models.Course(**course.dict())
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

@app.get("/courses/", response_model=List[schemas.CourseRead])
def list_courses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.Course).offset(skip).limit(limit).all()

@app.get("/courses/{course_id}", response_model=schemas.CourseRead)
def get_course(course_id: int, db: Session = Depends(get_db)):
    course = db.query(models.Course).filter(models.Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

@app.put("/courses/{course_id}", response_model=schemas.CourseRead)
def update_course(course_id: int, payload: schemas.CourseCreate, db: Session = Depends(get_db)):
    course = db.query(models.Course).filter(models.Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    for field, value in payload.dict().items():
        setattr(course, field, value)
    db.add(course)
    db.commit()
    db.refresh(course)
    return course

@app.delete("/courses/{course_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_course(course_id: int, db: Session = Depends(get_db)):
    course = db.query(models.Course).filter(models.Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    db.delete(course)
    db.commit()
    return

# ---------- Enrollment / relations ----------
@app.post("/students/{student_id}/enroll/{course_id}", response_model=schemas.StudentRead)
def enroll_student(student_id: int, course_id: int, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    course = db.query(models.Course).filter(models.Course.id == course_id).first()
    if not student or not course:
        raise HTTPException(status_code=404, detail="Student or Course not found")
    if course in student.courses:
        raise HTTPException(status_code=400, detail="Student already enrolled in this course")
    student.courses.append(course)
    db.commit()
    db.refresh(student)
    return student

@app.get("/students/{student_id}/courses", response_model=List[schemas.CourseRead])
def get_student_courses(student_id: int, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student.courses

@app.get("/courses/{course_id}/students", response_model=List[schemas.StudentRead])
def get_course_students(course_id: int, db: Session = Depends(get_db)):
    course = db.query(models.Course).filter(models.Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course.students
