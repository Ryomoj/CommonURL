from contextlib import asynccontextmanager
import logging
import sys
from pathlib import Path

from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

import uvicorn

from starlette.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from starlette.requests import Request

from connectors.redis_connector import redis_connector
from utils.dependencies import templates

sys.path.append(str(Path(__file__).parent.parent))

@asynccontextmanager
async def lifespan(app: FastAPI):
    await redis_connector.connect()
    FastAPICache.init(RedisBackend(redis_connector.redis), prefix="fastapi-cache")
    logging.info("FastAPI cache initialized")
    yield
    await redis_connector.disconnect()

app = FastAPI(lifespan=lifespan)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

from app.routers.links import router as links_router
app.include_router(links_router)

@app.get("/")
async def get_index_html(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0")