from datetime import datetime

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from db import Base


class LinksOrm(Base):
    __tablename__ = "links"

    id: Mapped[int] = mapped_column(primary_key=True)
    original_url: Mapped[str] = mapped_column(String(2083))
    short_code: Mapped[str] = mapped_column(String(228))
    created_at: Mapped[datetime]
