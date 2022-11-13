from database.ddl_base.ddl_composites import AlterTable, AlterColumn
from database.ddl_base.ddl_leafs import ColumnNotNull, ColumnDefault, Leaf
from database.dialects.mysql.mysql_ddl import ModifyColumn, NotNull, Default


def test_visit_alter_table(mysql_visitor, column):
    alter_table = AlterTable('users')
    alter_column = AlterColumn(column)

    not_null = ColumnNotNull()
    default = ColumnDefault('xd')

    alter_column.add_component(not_null)
    alter_column.add_component(default)

    alter_table.add_component(alter_column)

    for component_node in alter_table:
        component_node.accept(mysql_visitor)

    mysql_not_null = NotNull()
    mysql_default = Default(default.default)
    leaf = Leaf()

    modify_column = ModifyColumn(column)

    mysql_not_null.add_component(leaf)
    mysql_default.add_component(mysql_not_null)
    modify_column.add_component(mysql_default)

    assert len(alter_table.components) == 1
    assert alter_table.components[0] == modify_column
    assert list(alter_table) == [
        alter_table,
        modify_column,
        mysql_default,
        mysql_not_null,
        leaf,
        ]
