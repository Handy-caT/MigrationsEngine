from database.ddl_components_abstract import DDLLeaf
from schema.column import Column


class AddColumn(DDLLeaf):

    def __init__(self, column: Column):
        super().__init__()
        self.column = column

    def __repr__(self):
        return f'{self.__class__.__name__}({self.column!r})'

