from datetime import datetime

from fastapi import APIRouter, HTTPException, Form
from starlette.requests import Request
from starlette.responses import RedirectResponse

from app.schemas.links import LinkAddSchema, LinkResponseSchema, LinkSchemaWithCustomCode
from app.schemas.stats import StatsAddSchema
from app.utils.links_utils import generate_short_code
from app.utils.dependencies import DatabaseDep, templates

router = APIRouter(prefix="/links")

@router.post("/create_link/", description="Создать новую ссылку")
async def resize_new_url(
        request: Request,
        db: DatabaseDep,
        original_url: str = Form(),
        short_code: str = Form(None)
):
    data = LinkAddSchema(original_url=original_url, short_code=short_code)

    if not data.short_code:
        data.short_code = generate_short_code()
        new_code = data.short_code
        _data = LinkResponseSchema(
            created_at=datetime.now(),
            **data.model_dump()
        )

    else:
        new_code = data.short_code
        _data = LinkSchemaWithCustomCode(
            created_at=datetime.now(),
            **data.model_dump()
        )

    print(_data)
    await db.links.add_data(_data)
    await db.commit()
    new_short_link = f"http://127.0.0.1:8000/links/{new_code}"

    return templates.TemplateResponse("result.html", {
        "request": request,
        "short_url": new_short_link,
        "original_url": original_url
    })


@router.get("/{short_code}")
async def redirect_to_original(
    short_code: str,
    request: Request,
    db: DatabaseDep
):
    print(short_code)
    original_url = await db.links.get_url(short_code)
    if not original_url:
        raise HTTPException(status_code=404, detail="Link not found")

    statistics_data = StatsAddSchema(
        short_code=short_code,
        ip=request.client.host,
        user_agent=request.headers.get("user-agent"),
    )
    await db.stats.add_data(statistics_data)
    await db.commit()

    print(original_url)
    return RedirectResponse(original_url)