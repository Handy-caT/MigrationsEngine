from database.schema.column import Column
from database.schema.foreign_key import ForeignKey


class ColumnPlanBuilder:
    def __init__(self, column: Column, table_name: str) -> None:
        self.column = column
        self.table_name = table_name
        self._plan = {
            'Column': column,
        }

    @classmethod
    def from_dict(cls, adict: dict) -> 'ColumnPlanBuilder':
        return cls(adict['Column'], adict['TableName'])

    def get_plan(self) -> dict:
        return self._plan

    def add_unique(self) -> None:
        self._plan['Unique'] = 'Add'

    def drop_unique(self) -> None:
        self._plan['Unique'] = 'Drop'

    def add_not_null(self) -> None:
        self._plan['NotNull'] = 'Add'

    def add_default(self, default: str) -> None:
        self._plan['Default'] = {
            'Action': 'Add',
            'Value': default
        }

    def add_foreign_key(self, foreign_key: ForeignKey) -> None:
        self._plan['ForeignKey'] = {
            'Action': 'Add',
            'Table': foreign_key.key_table,
            'Column': foreign_key.key_column,
        }

    def drop_foreign_key(self) -> None:
        self._plan['ForeignKey'] = {
            'Action': 'Drop'
        }

    def drop_not_null(self) -> None:
        self._plan['NotNull'] = 'Drop'

    def drop_default(self) -> None:
        self._plan['Default'] = {
            'Action': 'Drop'
        }
