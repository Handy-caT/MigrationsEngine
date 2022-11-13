from typing import Optional, List

from database.schema.foreign_key import ForeignKey


class Column:
    def __init__(self, name: str, column_type: str, not_null: bool, key: Optional[str],
                 default: Optional[str], extra: Optional[str],
                 foreign_key: Optional[List[ForeignKey]] = None):
        self.name = name
        self.column_type = column_type.upper()
        self.not_null = not_null
        self.key = key
        self.default = default
        self.extra = extra
        self.foreign_key = foreign_key

    @classmethod
    def from_dict(cls, adict: dict):
        return Column(
            adict['Name'],
            adict['Type'],
            adict['NotNull'],
            adict['Key'],
            adict['Default'],
            adict['Extra'],
            adict['ForeignKey'],
        )

    def __copy__(self):
        return Column(
            self.name,
            self.column_type,
            self.not_null,
            self.key,
            self.default,
            self.extra,
            self.foreign_key,
        )

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name!r}, {self.column_type!r}, {self.not_null!r}, {self.key!r},' \
               f' {self.default!r}, {self.extra!r}, {self.foreign_key!r})'

    def __str__(self):
        return f'{self.__class__.__name__}: {self.name} {self.column_type}'
