import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# This pulls from the environment variable you set on Render
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

# Fallback for local development if DATABASE_URL is not set (e.g. sqlite)
if not SQLALCHEMY_DATABASE_URL:
    # Use SQLite for local dev if postgres url not found, or just warn.
    # For now, let's assume the user will set it or we default to sqlite
    SQLALCHEMY_DATABASE_URL = "sqlite:///./local_dev.db"
    # Note: connect_args={"check_same_thread": False} is needed only for SQLite

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    connect_args={"check_same_thread": False} if "sqlite" in SQLALCHEMY_DATABASE_URL else {}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency to get a DB session for each request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
