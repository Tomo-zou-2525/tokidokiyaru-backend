from pydantic_settings import BaseSettings


class DBSettings(BaseSettings):
    PGHOST: str
    PGPORT: str
    PGDATABASE: str
    PGUSER: str
    PGPASSWORD: str

    class ConfigDict:
        case_sensitive = True


db_settings = DBSettings()  # type: ignore

SQLALCHEMY_DATABASE_URL = \
    f"postgresql://{db_settings.PGUSER}:{db_settings.PGPASSWORD}@{db_settings.PGHOST}"
