from typing import Annotated

from fastapi import Depends
from starlette.templating import Jinja2Templates

from app.db import async_session_maker
from app.utils.db_manager import DBManager

templates = Jinja2Templates(directory="templates")

async def get_db():
    async with DBManager(session_factory=async_session_maker) as db:
        yield db


DatabaseDep = Annotated[DBManager, Depends(get_db)]