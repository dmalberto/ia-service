from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .config import Config

engine = create_engine(Config.db_url)
Session = sessionmaker(bind=engine)
