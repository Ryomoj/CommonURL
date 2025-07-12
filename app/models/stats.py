from sqlalchemy.orm import Mapped, mapped_column

from db import Base


class StatsOrm(Base):
    __tablename__ = "stats"

    id: Mapped[int] = mapped_column(primary_key=True)
    short_code: Mapped[str]
    ip: Mapped[str]
    user_agent: Mapped[str]
