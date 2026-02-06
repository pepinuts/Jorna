from __future__ import annotations

import logging
from typing import Any, Optional

from fastapi import HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.requests import Request

logger = logging.getLogger(__name__)


def make_error(message: str, status_code: int = 400, details: dict | None = None) -> dict:
    error_dict = {"error": { "status_code": status_code, "message": message }}
    if details:
        error_dict["error"]["details"] = details
    return error_dict

def http_exception_handler(request: Request, exc: HTTPException) -> JSONResponse:
    status=exc.status_code

    if status == 404:
        code = "NOT_FOUND"
    elif status == 401:
        code = "UNAUTHORIZED"
    elif status == 403:
        code = "FORBIDDEN"
    elif status == 400:
        code = "BAD_REQUEST"
    else:
        code = "HTTP_ERROR"

    message = exc.detail if isinstance(exc.detail, str) else "HTTP error"
    details = None if isinstance(exc.detail, str) else exc.detail

    return JSONResponse(
        status_code=status, content=make_error(message, status, details)
    )

def validation_exception_handler(request: Request, exc: RequestValidationError) -> JSONResponse:
    return JSONResponse(
        status_code=422,
        content=make_error(
            code="VALIDATION_ERROR",
            message="Invalid request",
            details=exc.errors(),
        ),
    )

def unhandled_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    logger.exception("Unhandled exception", exc_info=exc)
    return JSONResponse(
        status_code=500,
        content=make_error(code="INTERNAL_ERROR", message="Internal server error"),
    )