from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column

from db import Base


class LinksOrm(Base):
    __tablename__ = "links"

    id: Mapped[int] = mapped_column(primary_key=True)
    original_url: Mapped[str]
    short_code: Mapped[str]
    created_at: Mapped[datetime]
    # user_id: Mapped[int] = mapped_column(nullable=True) # Для пользователей с авторизацией
