import sqlalchemy.schema

from migration.abstract_schema_parser import AbstractSchemaParser
from schema.column import Column
from schema.database import Database
from schema.table import Table


class SQLAlchemySchemaParser(AbstractSchemaParser):

    def parse_column(self, column: sqlalchemy.schema.Column) -> Column:
        adict = {
            'Name': column.name,
            'Type': column.type,
            'NotNull': column.nullable,

        }
        if column.primary_key:
            adict['Key'] = 'PRI'
        elif column.unique:
            adict['Key'] = 'UNI'
        elif column.index:
            adict['Key'] = 'MUL'
        else:
            adict['Key'] = None

        pass

    def parse_table(self, table) -> Table:
        pass

    def parse_database(self, database) -> Database:
        pass
