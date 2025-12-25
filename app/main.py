from app.core.database import engine, Base
from fastapi import FastAPI
from app.core.config import settings
from app.api.v1.api import api_router

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/")
def home():
    return {"message": "Welcome to the Bistro API!"}