import abc
from abc import ABC

from database.visitors.abstract_visitor import AbstractNode, AbstractVisitor


class DDLComponent(ABC, AbstractNode):

    @property
    def is_composite(self):
        return False

    @abc.abstractmethod
    def __repr__(self):
        raise NotImplementedError

    def __iter__(self):
        return iter([])

    def accept(self, visitor: AbstractVisitor):
        visitor.visit(self)


class DDLComposite(DDLComponent, ABC):

    def __init__(self):
        self._components = []

    @property
    def is_composite(self):
        return True

    def add_component(self, component: DDLComponent):
        self._components.append(component)

    @property
    def components(self):
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


class DDLLeaf(DDLComponent, ABC):

    @abc.abstractmethod
    def __repr__(self):
        raise NotImplementedError

    def __iter__(self, depth=0):
        def gen(leaf):
            yield leaf, depth

        return gen(self)
