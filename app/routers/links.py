from datetime import datetime

from fastapi import APIRouter, HTTPException
from starlette.responses import RedirectResponse

from app.schemas.links import LinkAddSchema, LinkResponseSchema
from app.utils.links_utils import generate_short_code
from app.utils.dependencies import DatabaseDep

router = APIRouter(prefix="")

@router.post("/create_link/", description="Создать новую ссылку")
async def resize_new_url(data: LinkAddSchema, db: DatabaseDep):
    new_code = generate_short_code()
    _data = LinkResponseSchema(
        short_code=new_code,
        created_at=datetime.now(),
        **data.model_dump()
    )
    print(_data)
    await db.links.add_data(_data)
    await db.commit()
    new_short_link = f"http://127.0.0.1:8000/links/{new_code}"
    return {"new_short_link": new_short_link}


@router.get("/{short_code}")
async def redirect_to_original(
    short_code: str,
    # request: Request,  # Для доступа к данным запроса (IP, User-Agent)
    db: DatabaseDep
):
    print(short_code)
    original_url = await db.links.get_url(short_code)
    if not original_url:
        raise HTTPException(status_code=404, detail="Link not found")

    # Запись статистики в БД
    # await save_link_stats(
    #     short_code=short_code,
    #     ip=request.client.host,  # IP пользователя
    #     user_agent=request.headers.get("user-agent"),
    # )

    print(original_url)
    return RedirectResponse(original_url)