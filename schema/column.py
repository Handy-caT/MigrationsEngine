class Column:
    def __init__(self, name, column_type, not_null, key, default, extra):
        self.name = name
        self.column_type = column_type.lower()
        self.not_null = not_null
        self.key = key
        self.default = default
        self.extra = extra

    @classmethod
    def from_dict(cls, adict):
        return Column(
            adict['Name'],
            adict['Type'],
            adict['NotNull'],
            adict['Key'],
            adict['Default'],
            adict['Extra']
        )

