from database.ddl_base.ddl_composites import AlterColumn, AlterTable
from database.ddl_base.ddl_leafs import Leaf
from database.dialects.mysql.mysql_ddl import ModifyColumn, NotNull, Default
from database.visitors.abstract_visitor import AbstractVisitor

alter_column_dict = {
    'ColumnNotNull': (lambda component: NotNull(component.not_null)),
    'ColumnDefault': (lambda component: Default(component.default)),
}


class MySqlVisitor(AbstractVisitor):
    def visit_alter_table(self, node: AlterTable):
        for component in node.components:
            if isinstance(component, AlterColumn) and len(component.components) > 1:
                new_component = ModifyColumn(component.column)
                new_branch = Leaf()
                for sub_component in component.components:
                    temp = alter_column_dict\
                        .get(sub_component.__class__.__name__, (lambda x: x))(sub_component)
                    temp.add_component(new_branch)
                    new_branch = temp

                new_component.add_component(new_branch)

                node.remove_component(component)
                node.add_component(new_component)
