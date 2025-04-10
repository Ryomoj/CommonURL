from datetime import datetime

from pydantic import BaseModel, HttpUrl

class LinkSchema(BaseModel):
    original_url: HttpUrl  # Автоматическая валидация URL
    # custom_code: str | None = None  # Если пользователь хочет свой код


class LinkResponseSchema(BaseModel):
    short_url: str
    original_url: HttpUrl
    created_at: datetime