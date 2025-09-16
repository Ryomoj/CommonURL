from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_HOST: str = "database"
    DB_PORT: int = 5432
    DB_USER: str = "admin"
    DB_PASS: int = 0000
    DB_NAME: str = "commonurl"

    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379

    @property
    def REDIS_URL(self):
        return f"redis://{self.REDIS_HOST}:{self.REDIS_PORT}"

    @property
    def DB_URL(self):
        return "postgresql+asyncpg://admin:0000@database:5432/commonurl"


    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
