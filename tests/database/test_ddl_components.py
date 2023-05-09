from copy import deepcopy

from database.ddl_base.ddl_composites import Composite, AlterTable, AlterColumn
from database.ddl_base.ddl_leafs import ColumnNotNull, ColumnDefault, ShowColumns
from database.schema.column import Column


def test_iter_empty():
    composite = Composite()
    assert list(composite) == [composite]


def test_iter_leaf():
    leaf = ColumnNotNull()
    assert list(leaf) == [leaf]


def test_iter_composite(column):
    composite = Composite()

    alter_table = AlterTable('users')

    alter_column = AlterColumn(column)
    not_null = ColumnNotNull()
    alter_column.add_component(not_null)
    default = ColumnDefault('xd')
    alter_column.add_component(default)

    alter_table.add_component(alter_column)
    composite.add_component(alter_table)
    show_columns = ShowColumns('users')
    composite.add_component(show_columns)

    assert list(composite) == [
        composite,
        alter_table,
        alter_column,
        not_null,
        default,
        show_columns,
    ]


def test_copy_composite(composite_ddl):
    copy = deepcopy(composite_ddl)

    assert copy == composite_ddl
    assert copy is not composite_ddl


def test_composite_constructor():
    list_of_components = [
        ShowColumns('users'),
        ShowColumns('yolo'),
    ]

    composite = Composite(list_of_components)

    assert list(composite) == [
        composite,
        *list_of_components,
    ]


def test_composite_eq(composite_ddl):
    composite = Composite(AlterTable('users', False,
                                     AlterColumn(Column('password', 'VARCHAR(40)', False, None, None, None, None),
                                                 ColumnNotNull(True),
                                                 ColumnDefault('xd'))),
                          ShowColumns('users'))

    assert composite == composite_ddl
