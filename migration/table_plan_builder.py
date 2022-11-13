from typing import List

from database.schema.column import Column
from database.schema.exceptions import ColumnNotFoundException


class TablePlanBuilder:
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
    def from_dict(cls, adict: dict) -> 'TablePlanBuilder':
        return cls(
            table_name=adict['TableName'],
            columns=adict['Columns']
        )

    def get_plan(self) -> dict:
        return self._plan

    def add_column(self, column: Column) -> None:
        if column not in self.columns:
            raise ColumnNotFoundException(column)
        self._plan['ColumnsPlan'].append({
            'Column': column,
            'Action': 'Add'
        })

    def drop_column(self, column: Column) -> None:
        if column not in self.columns:
            raise ColumnNotFoundException(column)
        self._plan['ColumnsPlan'].append({
            'Column': column,
            'Action': 'Drop'
        })

    def add_index(self, column: Column) -> None:
        if column not in self.columns:
            raise ColumnNotFoundException(column)
        self._plan['IndexPlan'].append({
            'Column': column,
            'Action': 'Add'
        })

    def update_column(self, column: Column, column_plan: dict) -> None:
        if column not in self.columns:
            raise ColumnNotFoundException(column)
        self._plan['ColumnsPlan'].append({
            'Column': column,
            'Action': 'Update',
            'Plan': column_plan
        })
