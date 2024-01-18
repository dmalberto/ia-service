import os

from dotenv import load_dotenv


class Config:
    load_dotenv()
    db_url = os.getenv("DB_URL")
