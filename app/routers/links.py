from datetime import datetime
from urllib.request import Request

from fastapi import APIRouter, HTTPException
from starlette.responses import RedirectResponse

from app.schemas.links import LinkSchema, LinkResponseSchema
from app.services.links_service import generate_short_code
from app.utils.dependencies import DatabaseDep

router = APIRouter(prefix="/links")

@router.post("")
async def resize_new_url(data: LinkSchema, db: DatabaseDep):
    new_code = generate_short_code()
    _data = LinkResponseSchema(
        short_url=new_code,
        original_url=data.original_url,
        created_at=datetime.now()
    )
    new_data = await db.links.add_data(_data)
    return {"new_data": new_data}


@router.get("/{short_code}")
async def redirect_to_original(
    short_code: str,
    # request: Request,  # Для доступа к данным запроса (IP, User-Agent)
    db: DatabaseDep
):
    original_url = db.links.get_url(short_code)
    if not original_url:
        raise HTTPException(status_code=404, detail="Link not found")

    # Запись статистики в БД
    # await save_link_stats(
    #     short_code=short_code,
    #     ip=request.client.host,  # IP пользователя
    #     user_agent=request.headers.get("user-agent"),
    # )

    # Редирект с кодом 307
    return RedirectResponse(url=original_url, status_code=307)