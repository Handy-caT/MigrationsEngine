import abc


class AbstractVisitor:
    def visit(self, node):
        pass

    def visit_alter_table(self, node):
        pass

    def visit_alter_column(self, node):
        pass


class AbstractNode:
    @abc.abstractmethod
    def accept(self, visitor: AbstractVisitor):
        raise NotImplementedError
