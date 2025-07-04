import sys
from pathlib import Path

from fastapi import FastAPI
import uvicorn
from starlette.middleware.cors import CORSMiddleware

sys.path.append(str(Path(__file__).parent.parent))

from app.routers.links import router as links_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(links_router)


if __name__ == "__main__":
    uvicorn.run("main:app")