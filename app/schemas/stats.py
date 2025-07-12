from pydantic import BaseModel

class StatsAddSchema(BaseModel):
    short_code: str
    ip: str
    user_agent: str


class StatsSchema(StatsAddSchema):
    id: int