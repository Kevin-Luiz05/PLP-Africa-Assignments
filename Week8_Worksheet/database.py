# database.py
from sqlalchemy import create_engine                    # type: ignore
from sqlalchemy.ext.declarative import declarative_base # type: ignore
from sqlalchemy.orm import sessionmaker # type: ignore

# SQLite URL (file in project root)
SQLALCHEMY_DATABASE_URL = "sqlite:///./app.db"

# connect_args for SQLite to allow multithreading in dev
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
# SessionLocal class for DB sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
