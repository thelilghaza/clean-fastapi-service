from fastapi import FastAPI

from app.config import settings

app = FastAPI(title="Clean FastAPI Service")


@app.get("/health")
def health_check():
    return {"status": "healthy", "environment": settings.app_env}


@app.get("/")
def read_root():
    return {"message": "Welcome to the Clean DevOps API"}
