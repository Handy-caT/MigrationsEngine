class ForeignKey:
    def __init__(self, name: str, column_name: str, key_table: str, key_column: str) -> None:
        self.name = name
        self.column_name = column_name
        self.key_table = key_table
        self.key_column = key_column

    @classmethod
    def from_dict(cls, adict: dict) -> 'ForeignKey':
        return ForeignKey(
            adict['Name'],
            adict['Column'],
            adict['KeyTable'],
            adict['KeyColumn']
        )
