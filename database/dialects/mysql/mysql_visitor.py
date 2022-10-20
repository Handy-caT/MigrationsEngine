from database.ddl_base.ddl_composites import AlterColumn, AlterTable
from database.visitors.abstract_visitor import AbstractVisitor


class MySqlVisitor(AbstractVisitor):
    def visit_alter_table(self, node: AlterTable):
        

