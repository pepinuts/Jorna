from datetime import datetime, timezone
from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
def health():
    return {
        "status": "ok",
        "time_utc": datetime.now(timezone.utc).isoformat(),
    }
