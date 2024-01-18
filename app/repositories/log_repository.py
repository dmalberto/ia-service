from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, MetaData, String, Table, create_engine

from app.infra import Session


class LogRepository:
    def __init__(self, db_url):
        self.engine = create_engine(db_url)
        self.metadata = MetaData()

        self.logs_table = Table(
            "logs",
            self.metadata,
            Column("id", Integer, primary_key=True),
            Column("request", String),
            Column("response", String),
            Column("timestamp", DateTime),
        )

        self.metadata.create_all(self.engine)

        self.session = Session

    def log_request(self, request_data):
        self._log_to_db(str(request_data), "request")

    def log_response(self, response_data):
        self._log_to_db(str(response_data), "response")

    def _log_to_db(self, data, data_type):
        session = self.session()
        try:
            new_log = self.logs_table.insert().values(
                request=data if data_type == "request" else None,
                response=data if data_type == "response" else None,
                timestamp=datetime.now(),
            )
            session.execute(new_log)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
