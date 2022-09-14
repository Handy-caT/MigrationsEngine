class InvalidKeyInColumnException(Exception):
    def __init__(self, column_name):
        self.column_name = column_name

    def __str__(self):
        return f'If column {self.column_name} is a primary key, it must be not null'
