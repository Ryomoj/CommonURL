from fastapi import APIRouter, HTTPException, Form
from fastapi_cache.decorator import cache
from starlette.requests import Request
from starlette.responses import RedirectResponse

from app.utils.dependencies import DatabaseDep, templates
from services.links_service import LinksService

router = APIRouter(prefix="/links")

@router.post("/create_link/", description="Создать новую ссылку")
async def resize_new_url(
        request: Request,
        db: DatabaseDep,
        original_url: str = Form(),
        short_code: str = Form(None)
):
    new_short_link = await LinksService(db).resize_new_url(
        original_url=original_url,
        short_code=short_code)

    return templates.TemplateResponse("result.html", {
        "request": request,
        "short_url": new_short_link,
        "original_url": original_url
    })


@router.get("/{short_code}")
@cache(expire=10)
async def redirect_to_original(
    request: Request,
    short_code: str,
    db: DatabaseDep
):
    original_url = await LinksService(db).redirect_to_original(request, short_code=short_code)

    if not original_url:
        raise HTTPException(status_code=404, detail="Link not found")

    return RedirectResponse(original_url)