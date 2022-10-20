import abc

from database.ddl_base.ddl_composites import AlterTable, AlterColumn


class AbstractVisitor:
    def visit(self, node):
        pass

    def visit_alter_table(self, node: AlterTable):
        pass

    def visit_alter_column(self, node: AlterColumn):
        pass


class AbstractNode:
    @abc.abstractmethod
    def accept(self, visitor: AbstractVisitor):
        raise NotImplementedError
