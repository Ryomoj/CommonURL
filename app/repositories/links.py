from sqlalchemy import select

from app.models import LinksOrm
from app.repositories.base import BaseRepository
from app.schemas.links import LinkSchema


class LinksRepository(BaseRepository):
    model = LinksOrm
    schema = LinkSchema

    async def is_code_unique(self, code, ) -> bool:
        query = (self.session
                .select(self.model)
                .filter(self.model.short_code == code)
                .first())
        result = self.session.execute(query)
        return result is None


    async def get_url(self, short_code):
        query = select(self.model.original_url).filter_by(short_code=short_code)
        print(query)
        result = await self.session.execute(query)
        original_url = result.scalars().one()
        print(original_url)
        return original_url