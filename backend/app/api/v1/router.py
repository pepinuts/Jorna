from fastapi import APIRouter
from app.api.v1.routes.health import router as health_router
from app.api.v1.routes.version import router as version_router

api_router = APIRouter()
api_router.include_router(health_router, tags=["health"])
api_router.include_router(version_router, tags=["version"])
