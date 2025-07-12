import sys
from pathlib import Path

from fastapi import FastAPI
import uvicorn
from starlette.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from starlette.requests import Request

from utils.dependencies import templates

sys.path.append(str(Path(__file__).parent.parent))

from app.routers.links import router as links_router

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(links_router)

@app.get("/")
async def get_index_html(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


if __name__ == "__main__":
    uvicorn.run("main:app")