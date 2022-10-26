import sqlalchemy.schema

from migration.abstract_schema_parser import AbstractSchemaParser
from database.schema.column import Column
from database.schema.database import Database
from database.schema.foreign_key import ForeignKey
from database.schema.table import Table


class SQLAlchemySchemaParser(AbstractSchemaParser):

    def parse_column(self, column: sqlalchemy.schema.Column) -> Column:
        adict = {
            'Name': column.name,
            'Type': column.type.__str__(),
            'NotNull': not column.nullable,
        }
        if column.primary_key:
            adict['Key'] = 'PRI'
        elif column.unique:
            adict['Key'] = 'UNI'
        elif column.index:
            adict['Key'] = 'MUL'
        else:
            adict['Key'] = None

        if column.default:
            adict['Default'] = column.default
        else:
            adict['Default'] = None

        if column.autoincrement:
            adict['Extra'] = 'auto_increment'
        else:
            adict['Extra'] = None

        if column.foreign_keys:
            key = list(column.foreign_keys)[0]
            names = key.target_fullname.split('.')

            fk_name = 'fk_' + key.target_fullname.replace('.', '_')
            fk = ForeignKey(fk_name, column.name, names[0], names[1])
            adict['ForeignKey'] = fk
        else:
            adict['ForeignKey'] = None

        return Column.from_dict(adict)

    def parse_table(self, table) -> Table:
        pass

    def parse_database(self, database) -> Database:
        pass
