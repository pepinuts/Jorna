from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    BACKEND_CORS_ORIGINS: str = "http://localhost:5173"
    DATABASE_URL: str = "postgresql://app:app@db:5432/training"
    APP_NAME: str = "Training App API"
    APP_VERSION: str = "0.1.0"
    ENV: str = "local"

settings = Settings()
