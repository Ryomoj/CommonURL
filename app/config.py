from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_USER: str = "postgres"
    DB_PASS: int = 0000
    DB_NAME: str = "commonurl"


    @property
    def DB_URL(self):
        return "postgresql+asyncpg://postgres:0000@localhost:5432/commonurl"


    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
