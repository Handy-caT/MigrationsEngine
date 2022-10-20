from database.ddl_base.ddl_components_abstract import DDLComposite


class ModifyColumn(DDLComposite):
    def __init__(self, column_name: str):
        super().__init__()
        self.column_name = column_name

    def __repr__(self):
        return f'{self.__class__.__name__}({self.column_name}, {self._components!r})'


class NotNull(DDLComposite):
    def __init__(self, not_null: bool = True):
        super().__init__()
        self.not_null = not_null

    def __repr__(self):
        return f'{self.__class__.__name__}({self.not_null!r})'


class Default(DDLComposite):
    def __init__(self, default: str):
        super().__init__()
        self.default = default

    def __repr__(self):
        return f'{self.__class__.__name__}({self.default!r})'
