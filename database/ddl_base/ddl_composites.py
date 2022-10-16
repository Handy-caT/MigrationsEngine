from database.ddl_base.ddl_components_abstract import DDLComposite


class Composite(DDLComposite):
    def __init__(self, *args):
        super().__init__()
        for component in args:
            self._components.append(component)

    def __repr__(self):
        return f'{self.__class__.__name__}({self._components!r})'


class AlterTable(DDLComposite):

    def __init__(self, table_name: str, if_exists: bool = False):
        super().__init__()
        self.table_name = table_name
        self.if_exists = if_exists

    def __repr__(self):
        return f'{self.__class__.__name__}({self.table_name!r}, {self.if_exists!r}, {self._components!r})'


class AlterColumn(DDLComposite):

    def __init__(self, column_name: str):
        super().__init__()
        self.column_name = column_name

    def __repr__(self):
        return f'{self.__class__.__name__}({self.column_name!r}, {self._components!r})'


class AlterIndex(DDLComposite):

    def __init__(self, index: str, table_name: str):
        super().__init__()
        self.table_name = table_name
        self.index = index

    def __repr__(self):
        return f'{self.__class__.__name__}({self.table_name}, {self.index!r}, {self._components!r})'
