from abc import ABC

from database.ddl_base.ddl_components_abstract import DDLComposite, DDLComponent
from schema.column import Column


class TransitionDLL(DDLComposite, ABC):

    def add_component(self, component: DDLComponent):
        if len(self.components) == 0:
            super().add_component(component)
        else:
            raise Exception('TransitionDLL can have only one component')


class ModifyColumn(DDLComposite):
    def __init__(self, column: Column):
        super().__init__()
        self.column = column

    def __repr__(self):
        return f'{self.__class__.__name__}({self.column}, {self._components!r})'


class NotNull(TransitionDLL):
    def __init__(self, not_null: bool = True):
        super().__init__()
        self.not_null = not_null

    def __repr__(self):
        return f'{self.__class__.__name__}({self.not_null!r}, {self._components!r})'


class Default(TransitionDLL):
    def __init__(self, default: str):
        super().__init__()
        self.default = default

    def __repr__(self):
        return f'{self.__class__.__name__}({self.default!r}, {self._components!r})'
