from datetime import datetime

from pydantic import BaseModel, HttpUrl

class LinkAddSchema(BaseModel):
    original_url: str  # Автоматическая валидация URL
    # custom_code: str | None = None  # Если пользователь хочет свой код


class LinkResponseSchema(LinkAddSchema):
    short_code: str
    created_at: datetime


class LinkSchema(LinkResponseSchema):
    id: int