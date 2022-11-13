from datetime import timedelta

from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from pydantic import BaseSettings
from pydantic.config import Optional


class Settings(BaseSettings):
    DEBUG: Optional[str]
    DATABASE_URL: Optional[str]
    SECRET_KEY: str = "my_secret_key"
    LOG_LEVEL: str = "DEBUG"

    RESTX_VALIDATE: bool = True

    security_definitions = {
        'bearer': {
            'type': 'oauth2',
            'flow': 'password',
            'tokenUrl': '/login',
            'in': 'application/json'
        }
    }
    APISPEC_SPEC = APISpec(
        title='12 Factor App',
        version='v1',
        plugins=[MarshmallowPlugin()],
        openapi_version='2.0.0',
        securityDefinitions=security_definitions
    )
    APISPEC_SWAGGER_UI_URL = '/'

    JWT_SECRET_KEY: str = "secret_key"

    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)


settings = Settings(_env_file='.env', _env_file_encoding='utf-8')
