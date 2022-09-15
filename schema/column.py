class Column:
    def __init__(self, name: str, column_type: str, not_null: bool, key: str, default: str, extra: str):
        self.name = name
        self.column_type = column_type.lower()
        self.not_null = not_null
        self.key = key
        self.default = default
        self.extra = extra

    @classmethod
    def from_dict(cls, adict: dict):
        return Column(
            adict['Name'],
            adict['Type'],
            adict['NotNull'],
            adict['Key'],
            adict['Default'],
            adict['Extra']
        )

