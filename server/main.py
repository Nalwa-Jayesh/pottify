from fastapi import FastAPI

from database import engine
from models.base import Base
from routes import auth, song

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI Backend is Running!"}

app.include_router(auth.router, prefix='/auth')
app.include_router(song.router, prefix='/song')
Base.metadata.create_all(engine)