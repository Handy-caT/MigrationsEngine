from database.ddl_base.ddl_composites import AlterColumn, AlterTable
from database.ddl_base.ddl_leafs import Leaf, ColumnNotNull, ColumnDefault, DropDefault
from database.dialects.mysql.mysql_ddl import ModifyColumn, NotNull, Default
from database.abstract_visitor import BaseVisitor

alter_column_dict = {
    ColumnNotNull.__name__: (lambda component: NotNull(component.not_null)),
    ColumnDefault.__name__: (lambda component: Default(component.default)),
}


class MySqlVisitor(BaseVisitor):
    def visit_alter_table(self, node: AlterTable):
        for component in node.components:
            if isinstance(component, AlterColumn) and len(component.components) > 1:
                ex_components = []
                new_component = ModifyColumn(component.column)
                new_branch = Leaf()
                for sub_component in component.components:
                    if isinstance(sub_component, DropDefault):
                        ex_components.append(sub_component)
                    else:
                        temp = alter_column_dict\
                            .get(sub_component.__class__.__name__, (lambda x: x))(sub_component)
                        temp.add_component(new_branch)
                        new_branch = temp

                if len(ex_components) > 0:
                    alter_column = AlterColumn(component.column)
                    for ex_component in ex_components:
                        alter_column.add_component(ex_component)

                    node.add_component(alter_column)

                new_component.add_component(new_branch)

                node.remove_component(component)
                node.add_component(new_component)
