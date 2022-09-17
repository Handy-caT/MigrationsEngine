from typing import List

from schema.column import Column
from schema.exceptions import ColumnNotFoundException


class TablePlanGenerator:
    def _column_exists(self, column_name: str) -> bool:
        for column in self.columns:
            if column.name == column_name:
                return True
        return False

    def __init__(self, table_name: str, columns: List[Column]) -> None:
        self.table_name = table_name
        self.columns = columns
        self._plan = {
            'TableName': table_name,
            'ColumnsPlan': [],
            'IndexPlan': []
        }

    @classmethod
    def from_dict(cls, adict: dict) -> 'TablePlanGenerator':
        return cls(
            table_name=adict['TableName'],
            columns=adict['Columns']
        )

    def get_plan(self):
        return self._plan

    def alter_column(self, column_name: str) -> None:
        if not self._column_exists(column_name):
            raise ColumnNotFoundException(column_name)
        self._plan['ColumnsPlan'].append({
            'Column': column_name,
            'Action': 'Alter'
        })

    def drop_column(self, column_name: str) -> None:
        if not self._column_exists(column_name):
            raise ColumnNotFoundException(column_name)
        self._plan['ColumnsPlan'].append({
            'Column': column_name,
            'Action': 'Drop'
        })
