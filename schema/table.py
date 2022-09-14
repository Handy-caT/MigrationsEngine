from schema.exceptions.invalid_column_exception import InvalidKeyInColumnException


class Table:
    def _find_primary_key(self):
        for column in self.columns:
            if column.key == 'PRI':
                if not column.not_null:
                    raise InvalidKeyInColumnException(column.name)
                else:
                    self._primary_key.append(column.name)

    def _check_columns_unique(self):
        names = []
        columns = []

        for column in self.columns:
            if column.name not in names:
                columns.append(column)
                names.append(column.name)

        self.columns = columns

    def __init__(self, name, columns):
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

    def get_primary_key(self):
        return self._primary_key

    def set_primary_key(self, primary_key):
        for column_name in primary_key:
            for column in self.columns:
                if column.name == column_name:
                    column.key = 'PRI'
                    column.not_null = True

        self._primary_key = primary_key

    def add_column(self, column):
        self.columns.append(column)
        self._check_columns_unique()
