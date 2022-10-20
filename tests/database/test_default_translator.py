from database.ddl_base.ddl_composites import Composite, AlterColumn, AlterTable
from database.ddl_base.ddl_leafs import ShowColumns, ColumnNotNull


def test_leaf_translate(default_translator):
    leaf = ShowColumns('users')

    assert default_translator.translate(leaf) == ['SHOW COLUMNS FROM users;']


def test_line_translate(default_translator, column):
    alter_table = AlterTable('users')
    alter_column = AlterColumn(column)
    alter_column.add_component(ColumnNotNull())
    alter_table.add_component(alter_column)

    assert default_translator.translate(alter_table) == [
        f'ALTER TABLE users ALTER COLUMN {column.name} SET NOT NULL;'
    ]


def test_composite_translate(default_translator, composite_ddl, column):
    assert default_translator.translate(composite_ddl) == [
        f'ALTER TABLE users ALTER COLUMN {column.name} SET NOT NULL;',
        f'ALTER TABLE users ALTER COLUMN {column.name} SET DEFAULT xd;',
        'SHOW COLUMNS FROM users;'
    ]
