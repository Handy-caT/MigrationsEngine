from database.ddl_base.ddl_composites import Composite, AlterColumn, AlterTable
from database.ddl_base.ddl_leafs import ShowColumns, ColumnNotNull


def test_leaf_translate(default_translator):
    leaf = ShowColumns('users')

    assert default_translator.translate(leaf) == ['SHOW COLUMNS FROM users;']


def test_line_translate(default_translator):
    alter_table = AlterTable('users')
    alter_column = AlterColumn('data')
    alter_column.add_component(ColumnNotNull())
    alter_table.add_component(alter_column)

    assert default_translator.translate(alter_table) == [
        'ALTER TABLE users ALTER COLUMN data SET NOT NULL;'
    ]


def test_composite_translate(default_translator, composite_ddl):
    assert default_translator.translate(composite_ddl) == [
        'ALTER TABLE users ALTER COLUMN data SET NOT NULL;',
        'ALTER TABLE users ALTER COLUMN data SET DEFAULT xd;',
        'SHOW COLUMNS FROM users;'
    ]
