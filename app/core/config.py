from pydantic import AnyHttpUrl, BaseSettings, EmailStr, validator
from typing import Optional, List, Union
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    JWT_SECRET_KEY: str = "secret"
    ALGORITHM: str = "HS256"

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8 # 8 days
    BACKEND_CORS_ORIGINS: Optional[List[AnyHttpUrl]] = []

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    SQL_ALCHEMY_DATABASE_URI: Optional[str] = "sqlite:///hapy.db"
    FIRST_SUPERUSER: Optional[EmailStr] = "superadmin@hapyapi.com"
    FIRST_SUPERUSER_PASSWORD: Optional[str] = "passworddummy7454545877!M"

    class Config:
        case_sensitive = True


settings = Settings()
