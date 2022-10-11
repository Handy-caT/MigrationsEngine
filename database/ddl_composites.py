from database.ddl_components_abstract import DDLComposite, DDLComponent, DDLLeaf
from schema.column import Column


class AlterTable(DDLComposite):

    def __init__(self, table_name: str, if_exists: bool = False):
        super().__init__()
        self.table_name = table_name
        self.if_exists = if_exists

    def __repr__(self):
        return f'{self.__class__.__name__}({self.table_name!r}, {self.if_exists!r}, {self._components!r})'

