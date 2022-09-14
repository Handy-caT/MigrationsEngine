class Database:
    def __init__(self, name, tables):
        self.name = name
        self.tables = tables

    @classmethod
    def from_dict(cls, adict):
        return cls(
            name=adict['Name'],
            tables=adict['Tables']
        )
