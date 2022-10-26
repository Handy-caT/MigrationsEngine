import abc

from database.schema.column import Column
from database.schema.database import Database
from database.schema.table import Table


class AbstractSchemaParser:

    @abc.abstractmethod
    def parse_column(self, column) -> Column:
        raise NotImplementedError

    @abc.abstractmethod
    def parse_table(self, table) -> Table:
        raise NotImplementedError

    @abc.abstractmethod
    def parse_database(self, database) -> Database:
        raise NotImplementedError
