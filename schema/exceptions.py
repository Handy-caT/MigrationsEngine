class ColumnNotFoundException(Exception):
    def __init__(self, column_name):
        self.column_name = column_name

    def __str__(self):
        return "Column not found: " + self.column_name


class InvalidColumnException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class InvalidTableException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
