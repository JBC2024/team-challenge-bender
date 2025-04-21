import os, requests
from fastapi import APIRouter, HTTPException, status

router = APIRouter(prefix="/api/v1")
HOOK = os.getenv("REDEPLOY_HOOK")

@router.post("/redeploy", status_code=status.HTTP_202_ACCEPTED)
def redeploy():
    r = requests.post(HOOK, timeout=10)
    if r.status_code not in (200, 201, 202):
        raise HTTPException(500, f"Hook falló: {r.text}")
    return {"detail": "Deploy solicitado correctamente"}
