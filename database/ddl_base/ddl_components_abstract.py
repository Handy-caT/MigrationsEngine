import abc
from abc import ABC


class DDLComponent(ABC):

    @property
    def is_composite(self):
        return False

    @abc.abstractmethod
    def __repr__(self):
        raise NotImplementedError


class DDLComposite(DDLComponent, ABC):

    def __init__(self):
        self._components = []

    @property
    def is_composite(self):
        return True

    def add_component(self, component: DDLComponent):
        self._components.append(component)

    def get_components(self):
        return self._components

    def remove_component(self, component: DDLComponent):
        self._components.remove(component)

    @abc.abstractmethod
    def __repr__(self):
        raise NotImplementedError


class DDLLeaf(DDLComponent, ABC):

    @abc.abstractmethod
    def __repr__(self):
        raise NotImplementedError
