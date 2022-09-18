class ColumnPlanBuilder:
    def __init__(self, column_name, table_name):
        self.column_name = column_name
        self.table_name = table_name
        self._plan = {
            'ColumnName': column_name
        }

    @classmethod
    def from_dict(cls, adict):
        return cls(adict['ColumnName'], adict['TableName'])

    def get_plan(self):
        return self._plan

    def add_unique(self):
        self._plan['Unique'] = 'Add'

    def drop_unique(self):
        self._plan['Unique'] = 'Drop'

    def add_not_null(self):
        self._plan['NotNull'] = 'Add'

    def add_default(self, default: str):
        self._plan['Default'] = {
            'Action': 'Add',
            'Value': default
        }

    def add_foreign_key(self, key_table: str, key_column: str):
        self._plan['ForeignKey'] = {
            'Action': 'Add',
            'Table': key_table,
            'Column': key_column
        }

    def drop_foreign_key(self):
        self._plan['ForeignKey'] = {
            'Action': 'Drop'
        }

    def drop_not_null(self):
        self._plan['NotNull'] = 'Drop'

    def drop_default(self):
        self._plan['Default'] = {
            'Action': 'Drop'
        }
