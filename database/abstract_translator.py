import abc
from abc import ABC

from database.ddl_base.ddl_components_abstract import DDLComponent


class AbstractTranslator(ABC):

    @abc.abstractmethod
    @property
    def dialect(self):
        raise NotImplementedError

    @abc.abstractmethod
    def translate(self, ddl_component: DDLComponent):
        raise NotImplementedError

