from app.models.stats import StatsOrm
from app.repositories.base import BaseRepository
from app.schemas.stats import StatsSchema


class StatsRepository(BaseRepository):
    model = StatsOrm
    schema = StatsSchema



