from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
import logging
from app.core.logging import setup_logging
from app.core.errors import http_exception_handler, unhandled_exception_handler, validation_exception_handler
from fastapi.exceptions import RequestValidationError
from fastapi import HTTPException
from app.api.v1.router import api_router

setup_logging(settings.ENV)

logger=logging.getLogger(__name__)
logger.info("Starting API", extra={"env": settings.ENV, "version": settings.APP_VERSION})


app = FastAPI(title=settings.APP_NAME, version=settings.APP_VERSION)

app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(Exception, unhandled_exception_handler)


# CORS (front local)
origins = [o.strip() for o in settings.BACKEND_CORS_ORIGINS.split(",") if o.strip()]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins or ["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api/v1")

@app.get("/", tags=["root"])
def root():
    return {"name": "Training App API", "docs": "/docs"}
