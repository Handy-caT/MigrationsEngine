from typing import List


class Index:
    def __init__(self, name: str, columns: List[str], unique: bool) -> None:
        self.name = name
        self.columns = columns
        self.unique = unique

    @classmethod
    def from_dict(cls, adict: dict) -> 'Index':
        return Index(
            adict['Name'],
            adict['Columns'],
            adict['Unique']
        )
