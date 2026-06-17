from pymongo import MongoClient
from app.core.config import settings

client: MongoClient | None = None


def init_db():
    global client
    client = MongoClient(settings.mongodb_uri)


def close_db():
    global client
    if client:
        client.close()
        client = None


def get_db():
    if client is None:
        raise RuntimeError("Database not initialized")
    return client[settings.database_name]
