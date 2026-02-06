from datetime import datetime, timezone
from fastapi import APIRouter
from app.core.config import settings

router = APIRouter()

@router.get("/version")
def version():
    return {
        "name": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "commit":"",
    }
