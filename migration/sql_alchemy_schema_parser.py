import sqlalchemy.schema

from migration.abstract_schema_parser import AbstractSchemaParser
from schema.column import Column
from schema.database import Database
from schema.table import Table


class SQLAlchemySchemaParser(AbstractSchemaParser):

    def parse_column(self, column: sqlalchemy.schema.Column) -> Column:
        adict = {

        }
        pass

    def parse_table(self, table) -> Table:
        pass

    def parse_database(self, database) -> Database:
        pass
