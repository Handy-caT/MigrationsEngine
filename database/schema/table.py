from typing import List, Optional

from database.schema.column import Column
from database.schema.exceptions import InvalidColumnException, ColumnNotFoundException, IndexNotFoundException
from database.schema.foreign_key import ForeignKey
from database.schema.index import Index


class Table:
    def _find_primary_key(self):
        for column in self.columns:
            if column.key == 'PRI':
                if not column.not_null:
                    raise InvalidColumnException(f'Primary key in {column.name} must be not null')

                self._primary_key.append(column.name)

    def _find_foreign_key(self):
        for column in self.columns:
            if column.foreign_key:
                if column.key != 'MUL':
                    raise InvalidColumnException(f'Foreign key in {column.name} must be a multiple key')

                self._foreign_key.append(column.foreign_key)

    def _check_columns_unique(self):
        names = []
        columns = []

        for column in self.columns:
            if column.name not in names:
                columns.append(column)
                names.append(column.name)

        self.columns = columns

    def __init__(self, name: str, columns: List[Column], index: Optional[List[Index]] = None) -> None:
        self.name = name
        self.columns = columns
        self.index = index
        self._primary_key = []
        self._foreign_key = []
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

    def drop_column(self, column_name: str):
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

    def __copy__(self) -> 'Table':
        return Table(
            name=self.name,
            columns=self.columns.copy()
        )

    def add_index(self, index: Index) -> None:
        self.index.append(index)

    def drop_index(self, index_name: str) -> None:
        deleted = False

        for index in self.index:
            if index.name == index_name:
                self.index.remove(index)
                deleted = True
                break

        if not deleted:
            raise IndexNotFoundException(index_name)

    def add_foreign_key(self, foreign_key: ForeignKey):
        for column in self.columns:
            if column.name == foreign_key.column_name:
                if column.key == 'PRI':
                    raise InvalidColumnException(f"Can't add {foreign_key} to {column}"
                                                 f" because it has primary key")
                else:
                    pass

                self._foreign_key.append(foreign_key)
                column.foreign_key = foreign_key
                break

    @property
    def column_names(self):
        return [column.name for column in self.columns]

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name!r}, {self.columns!r}, {self.index!r})'

    def __str__(self):
        return f'{self.__class__.__name__}: {self.name}'

    def __iter__(self):
        return iter(self.columns)
