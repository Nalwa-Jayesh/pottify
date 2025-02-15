import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from dotenv import load_dotenv
from models.base import Base

# Load environment variables
load_dotenv()

# Ensure DATABASE_URL is loaded
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set in the environment variables")

# Create engine
engine = create_engine(DATABASE_URL, echo=True)  # Set echo=True for debug logs

# Use scoped_session for thread safety
SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

# Dependency function for FastAPI routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

