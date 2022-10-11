from sqlalchemy import create_engine


class Engine:
    def __init__(self, db_url: str):
        self.db_url = db_url
        self._engine = create_engine(db_url, echo=True, pool_size=10, pool_recycle=3600)

    @property
    def dialect(self):
        part = self.db_url.split(':')[0]
        return part.split('+')[0].lower()

    def get_connection(self):
        return self._engine.connect()
    