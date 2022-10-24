import abc
from abc import ABC

from database.abstract_visitor import AbstractNode, BaseVisitor


class DDLComponent(ABC, AbstractNode):

    @property
    def is_composite(self):
        return False

    @abc.abstractmethod
    def __repr__(self):
        raise NotImplementedError

    def __iter__(self):
        return iter([])

    def accept(self, visitor: BaseVisitor):
        visitor.visit(self)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


class DDLComposite(DDLComponent, ABC):

    def __init__(self):
        self._components: list[DDLComponent] = []

    @property
    def is_composite(self):
        return True

    def add_component(self, component: DDLComponent):
        self._components.append(component)

    @property
    def components(self) -> list[DDLComponent]:
        return self._components

    def remove_component(self, component: DDLComponent):
        self._components.remove(component)

    @abc.abstractmethod
    def __repr__(self):
        raise NotImplementedError

    def __iter__(self, depth=0):
        def gen(composite):
            yield composite, depth
            for component in composite.components:
                iterator = component.__iter__(depth + 1)
                try:
                    yield from iterator
                except StopIteration:
                    pass

        return gen(self)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


class DDLLeaf(DDLComponent, ABC):

    @abc.abstractmethod
    def __repr__(self):
        raise NotImplementedError

    def __iter__(self, depth=0):
        def gen(leaf):
            yield leaf, depth

        return gen(self)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
