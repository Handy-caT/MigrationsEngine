class Column:
    def __init__(self, name, column_type, null, key, default, extra):
        self.name = name
        self.column_type = column_type.lower()
        self.null = null
        self.key = key
        self.default = default
        self.extra = extra

    @classmethod
    def from_dict(cls, adict):
        return Column(
            adict['Name'],
            adict['Type'],
            adict['Null'],
            adict['Key'],
            adict['Default'],
            adict['Extra']
        )
