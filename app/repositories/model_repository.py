from sqlalchemy import Boolean, Column, Integer, MetaData, String, Table, create_engine
from sqlalchemy.sql import select

from app.adapters import ModelLoader
from app.infra import Session


class ModelRepository:
    def __init__(self, db_url):
        self.engine = create_engine(db_url)
        self.metadata = MetaData()
        self.session = Session

        self.models_table = Table(
            "ml_models",
            self.metadata,
            Column("id", Integer, primary_key=True),
            Column("model_path", String),
            Column("active", Boolean),
        )

        self.metadata.create_all(self.engine)

    def get_current_model_path(self):
        with self.session() as session:
            query = select([self.models_table.c.model_path]).where(
                self.models_table.c.active == True
            )
            result = session.execute(query).scalar()
            return result

    def get_model(self):
        model_path = self.get_current_model_path()
        return ModelLoader.load_model(model_path)
