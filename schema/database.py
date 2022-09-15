from schema.exceptions.invalid_table_exception import InvalidTableException


class Database:

    def _check_tables_unique(self):
        names = []
        tables = []

        for table in self.tables:
            if table.name not in names:
                tables.append(table)
                names.append(table.name)

        self.tables = tables

    def __init__(self, name, tables):
        self.name = name
        self.tables = tables
        self._check_tables_unique()

    @classmethod
    def from_dict(cls, adict):
        return cls(
            name=adict['Name'],
            tables=adict['Tables']
        )

    def add_table(self, table):
        self.tables.append(table)
        self._check_tables_unique()

    def remove_table(self, table_name):
        deleted = False

        for table in self.tables:
            if table.name == table_name:
                self.tables.remove(table)
                deleted = True
                break

        if not deleted:
            raise InvalidTableException(f'No table named {table_name} in database {self.name}')
