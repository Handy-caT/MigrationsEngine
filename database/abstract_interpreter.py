import abc

from database.ddl_base.ddl_components_abstract import DDLComponent


class AbstractInterpreter:

    @abc.abstractmethod
    def interpret(self, component: DDLComponent):
        raise NotImplementedError
