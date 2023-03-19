import time
import http
import hashlib
import hmac
import os

from fastapi import FastAPI, APIRouter, Query, HTTPException, Request, Depends, Response, Header
from fastapi.templating import Jinja2Templates
from typing import Optional, Any
from pathlib import Path
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from app.api.api_v1.api import api_router
from app.core.config import settings

BASE_PATH = Path(__file__).resolve().parent

TEMPLATES = Jinja2Templates(directory=str(BASE_PATH / "templates"))

app = FastAPI(
    title="Hâpy API",
    description="Hâpy Checkout System Restful API.",
    version="0.1.0",
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    docs_url="/docs",
    debug=True,
)

def generate_hash_signature(secret_key: bytes, payload: bytes, digest_method=hashlib.sha1) -> str:
    return hmac.new(
        secret_key,
        payload,
        digest_method,
    ).hexdigest()

root_router = APIRouter()

@root_router.get('/', status_code=200)
def root(request: Request) -> dict:
    return TEMPLATES.TemplateResponse("index.html", { "request": request })


@app.post("/orders.notify", status_code=200)
async def webhook(request: Request, x_hub_signature: str = Header(None)):
    payload = await request.body()
    secret_key = settings.WEBHOOK_SECRET_KEY.encode("utf-8")
    signature = generate_hash_signature(secret_key, payload)
    if x_hub_signature != f"sha1={signature}":
        raise HTTPException(
            status_code=400,
            detail="Invalid signature",
        )
    return {}

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

app.include_router(api_router, prefix=settings.API_V1_STR)
app.include_router(root_router)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")