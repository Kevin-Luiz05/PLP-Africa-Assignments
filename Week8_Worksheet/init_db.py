# init_db.py
from database import SessionLocal, engine
import models

# create tables (safe)
models.Base.metadata.create_all(bind=engine)

def init_sample():
    db = SessionLocal()
    # avoid duplicates on re-run
    if db.query(models.Student).count() == 0 and db.query(models.Course).count() == 0:
        s1 = models.Student(first_name="Alice", last_name="Njeri", email="alice@example.com", age=20)
        s2 = models.Student(first_name="Brian", last_name="Otieno", email="brian@example.com", age=22)
        c1 = models.Course(title="Intro to Python", description="Learn the basics of Python.", credits=3)
        c2 = models.Course(title="Databases 101", description="Relational databases and SQL.", credits=2)
        db.add_all([s1, s2, c1, c2])
        db.commit()
        # enroll Alice in Python
        s1.courses.append(c1)
        db.commit()
        print("Sample data created.")
    else:
        print("Sample data already exists.")
    db.close()

if __name__ == "__main__":
    init_sample()
