from database.ddl_base.ddl_components_abstract import DDLLeaf
from database.schema.column import Column
from database.schema.foreign_key import ForeignKey
from database.schema.index import Index


class Leaf(DDLLeaf):
    def __init__(self):
        super().__init__()

    def __repr__(self):
        return f'{self.__class__.__name__}()'


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

    def __init__(self, default: str = None):
        super().__init__()
        self.default = default

    def __repr__(self):
        return f'{self.__class__.__name__}({self.default!r})'


class ColumnNotNull(DDLLeaf):

    def __init__(self, not_null: bool = True):
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


class AddForeignKey(DDLLeaf):

    def __init__(self, foreign_key: ForeignKey):
        super().__init__()
        self.foreign_key = foreign_key

    def __repr__(self):
        return f'{self.__class__.__name__}({self.foreign_key!r})'


class ColumnUnique(DDLLeaf):

    def __init__(self, unique: Index):
        super().__init__()
        self.unique = unique

    def __repr__(self):
        return f'{self.__class__.__name__}({self.unique!r})'


class DropConstraint(DDLLeaf):

    def __init__(self, constraint_name: str):

        super().__init__()
        self.constraint_name = constraint_name

    def __repr__(self):
        return f'{self.__class__.__name__}({self.constraint_name!r})'


class DropIndex(DDLLeaf):

    def __init__(self, index_name: str, table_name: str = None):
        super().__init__()
        self.index_name = index_name
        self.table_name = table_name

    def __repr__(self):
        return f'{self.__class__.__name__}({self.table_name}, {self.index_name!r})'


class DropTable(DDLLeaf):

    def __init__(self, table_name: str):
        super().__init__()
        self.table_name = table_name

    def __repr__(self):
        return f'{self.__class__.__name__}({self.table_name!r})'


class ShowColumns(DDLLeaf):

    def __init__(self, table_name: str):
        super().__init__()
        self.table_name = table_name

    def __repr__(self):
        return f'{self.__class__.__name__}({self.table_name!r})'


class CreateIndex(DDLLeaf):

    def __init__(self, index: Index, table_name: str = None):
        super().__init__()
        self.index = index
        self.table_name = table_name

    def __repr__(self):
        return f'{self.__class__.__name__}({self.table_name}, {self.index!r})'


class DropDefault(DDLLeaf):
    def __init__(self):
        super().__init__()

    def __repr__(self):
        return f'{self.__class__.__name__}()'
