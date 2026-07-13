from fastapi import FastAPI

from app.core.config import settings
from app.api.v1.chat import router as chat_router

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)
app.include_router(
    chat_router,
    prefix="/api/v1",
    tags=["Chat"]
)


@app.get("/")
def root():
    return {
        "message": "Enterprise AI Copilot API Running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }