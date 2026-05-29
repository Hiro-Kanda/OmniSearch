from fastapi import FastAPI

from app.api.health import router as health_router
from app.api.sharepoint import router as sharepoint_router

app = FastAPI(title="RAG SharePoint API")

app.include_router(health_router, prefix="/api")
app.include_router(sharepoint_router, prefix="/api")