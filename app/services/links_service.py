from datetime import datetime

from starlette.requests import Request

from schemas.links import LinkSchemaWithCustomCode, LinkResponseSchema, LinkAddSchema
from schemas.stats import StatsAddSchema
from services.base import BaseService
from utils.links_utils import generate_short_code


class LinksService(BaseService):

    async def resize_new_url(
            self,
            original_url: str,
            short_code: str
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

        await self.db.links.add_data(_data)
        await self.db.commit()
        new_short_link = f"http://127.0.0.1:8000/links/{new_code}"

        return new_short_link


    async def redirect_to_original(
            self,
            request: Request,
            short_code: str
    ):
        original_url = await self.db.links.get_url(short_code)

        statistics_data = StatsAddSchema(
            short_code=short_code,
            ip=request.client.host,
            user_agent=request.headers.get("user-agent"),
        )
        await self.db.stats.add_data(statistics_data)
        await self.db.commit()

        return original_url