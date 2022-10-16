from database.ddl_base.ddl_composites import Composite, AlterTable, AlterColumn
from database.ddl_base.ddl_leafs import ColumnNotNull, ColumnDefault, ShowColumns


def test_iter_empty():
    composite = Composite()
    assert list(composite) == [(composite, 0)]


def test_iter_leaf():
    leaf = ColumnNotNull()
    assert list(leaf) == [(leaf, 0)]


def test_iter_composite():
    composite = Composite()

    alter_table = AlterTable('users')

    alter_column = AlterColumn('data')
    not_null = ColumnNotNull()
    alter_column.add_component(not_null)
    default = ColumnDefault('xd')
    alter_column.add_component(default)

    alter_table.add_component(alter_column)
    composite.add_component(alter_table)
    show_columns = ShowColumns('users')
    composite.add_component(show_columns)

    assert list(composite) == [
        (composite, 0),
        (alter_table, 1),
        (alter_column, 2),
        (not_null, 3),
        (default, 3),
        (show_columns, 1)
    ]
