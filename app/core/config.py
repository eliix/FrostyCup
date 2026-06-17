from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):

    mongodb_uri: str = "mongodb://localhost:27017"  ## default uri
    database_name: str = "monguito_db"  # default name

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8"}


settings = Settings()
