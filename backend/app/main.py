from fastapi import FastAPI
from sqlalchemy import text
from backend.app.database.connection import Base,engine
from backend.app.models.user import User
app=FastAPI(title="Online Examination System",description="API for an online quiz and examination system",version="1.0.0")
Base.metadata.create_all(bind=engine)
@app.get("/")


def home():
    return{"message":"Online Examination System APIis running!"}

@app.get("/health")
def health_check():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        return {
            "status": "healthy",
            "database": "connected"
        }

    except Exception as e:
        return {
            "status": "unhealthy",
            "database": "disconnected",
            "error": str(e)
        }