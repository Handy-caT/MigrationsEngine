from database.ddl_components_abstract import DDLLeaf
from schema.column import Column


class AddColumn(DDLLeaf):

    def __init__(self, column: Column):
        super().__init__()
        self.column = column

    def __repr__(self):
        return f'{self.__class__.__name__}({self.column!r})'


class ColumnType(DDLLeaf):

    def __init__(self, column_type: str):
        super().__init__()
        self.column_type = column_type

    def __repr__(self):
        return f'{self.__class__.__name__}({self.column_type!r})'


class ColumnDefault(DDLLeaf):

    def __init__(self, default: str):
        super().__init__()
        self.default = default

    def __repr__(self):
        return f'{self.__class__.__name__}({self.default!r})'


class ColumnNotNull(DDLLeaf):

    def __init__(self, not_null: bool):
        super().__init__()
        self.not_null = not_null

    def __repr__(self):
        return f'{self.__class__.__name__}({self.not_null!r})'


class DropColumn(DDLLeaf):

    def __init__(self, column_name: str):
        super().__init__()
        self.column_name = column_name

    def __repr__(self):
        return f'{self.__class__.__name__}({self.column_name!r})'


class RenameColumn(DDLLeaf):

    def __init__(self, old_name: str, new_name: str):
        super().__init__()
        self.old_name = old_name
        self.new_name = new_name

    def __repr__(self):
        return f'{self.__class__.__name__}({self.old_name!r}, {self.new_name!r})'


class RenameTable(DDLLeaf):

    def __init__(self, old_name: str, new_name: str):
        super().__init__()
        self.old_name = old_name
        self.new_name = new_name

    def __repr__(self):
        return f'{self.__class__.__name__}({self.old_name!r}, {self.new_name!r})'
    