from os import getenv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class ServiceBase:
    def __init__(self):
        self._session = None
        self.engine = None

    def _init_connection(self):
        self.engine = create_engine(
            f'postgresql://{getenv("DB_USER")}:{getenv("DB_PASS")}@{getenv("RDS_ENDPOINT")}:5432/postgres',
            pool_size=1,
            echo=True
        )

    def get_session(self):
        if self._session is not None:
            return self._session

        session = sessionmaker()
        session.configure(bind=self.engine)
        self._session = session()
        return self._session
