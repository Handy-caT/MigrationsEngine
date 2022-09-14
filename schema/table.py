class Table:
    def __init__(self, name, columns, primary_key):
        self.name = name
        self.columns = columns
        self.primary_key = primary_key

    @classmethod
    def from_dict(cls, adict):
        return cls(
            name=adict['Name'],
            columns=adict['Columns'],
            primary_key=adict['PrimaryKey']
        )
