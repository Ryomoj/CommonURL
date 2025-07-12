from datetime import datetime

from pydantic import BaseModel

class LinkAddSchema(BaseModel):
    original_url: str
    short_code: str | None = None  # Если пользователь хочет свой код


class LinkResponseSchema(LinkAddSchema):
    short_code: str
    created_at: datetime

class LinkSchemaWithCustomCode(LinkAddSchema):
    created_at: datetime


class LinkSchema(LinkResponseSchema):
    id: int