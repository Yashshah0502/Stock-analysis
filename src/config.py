"""Configuration management using pydantic-settings."""
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Load settings from .env file."""

    model_config = SettingsConfigDict(env_file=".env", case_sensitive=False)

    finnhub_api_key: str = ""
    fmp_api_key: str = ""
    polygon_api_key: str = ""
    sec_user_agent: str = ""


_settings: Settings | None = None


def get_settings() -> Settings:
    """Get or create settings singleton."""
    global _settings
    if _settings is None:
        _settings = Settings()
    return _settings
