from typing import List

from schema.column import Column
from schema.exceptions import InvalidColumnException, ColumnNotFoundException


class Table:
    def _find_primary_key(self):
        for column in self.columns:
            if column.key == 'PRI':
                if not column.not_null:
                    raise InvalidColumnException(f'Primary key in {column.name} must be not null')

                self._primary_key.append(column.name)

    def _check_columns_unique(self):
        names = []
        columns = []

        for column in self.columns:
            if column.name not in names:
                columns.append(column)
                names.append(column.name)

        self.columns = columns

    def __init__(self, name: str, columns: List[Column]):
        self.name = name
        self.columns = columns
        self._primary_key = []
        self._find_primary_key()
        self._check_columns_unique()

    @classmethod
    def from_dict(cls, adict):
        return cls(
            name=adict['Name'],
            columns=adict['Columns']
        )

    def get_primary_key(self) -> List[str]:
        return self._primary_key

    def set_primary_key(self, primary_key: List[str]):
        for column_name in primary_key:
            for column in self.columns:
                if column.name == column_name:
                    column.key = 'PRI'
                    column.not_null = True

        self._primary_key = primary_key

    def add_column(self, column: Column):
        self.columns.append(column)
        self._check_columns_unique()

    def remove_column(self, column_name: str):
        deleted = False

        for column in self.columns:
            if column.name == column_name:
                if column.key == 'PRI' and len(self._primary_key) == 1:
                    raise InvalidColumnException(f'Cannot remove only primary key in {column_name}')
                self.columns.remove(column)
                deleted = True
                break

        if not deleted:
            raise ColumnNotFoundException(column_name)

    def get_column(self, column_name: str) -> Column:
        for column in self.columns:
            if column.name == column_name:
                return column

        raise ColumnNotFoundException(column_name)

    def __copy__(self):
        return Table(
            name=self.name,
            columns=self.columns.copy()
        )

    @property
    def column_names(self):
        return [column.name for column in self.columns]
