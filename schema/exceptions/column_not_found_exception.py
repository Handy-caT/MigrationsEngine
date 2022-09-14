class ColumnNotFoundException(Exception):
    def __init__(self, column_name):
        self.column_name = column_name

    def __str__(self):
        return "Column not found: " + self.column_name
