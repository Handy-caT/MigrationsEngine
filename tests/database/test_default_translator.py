from database.ddl_base.ddl_composites import Composite, AlterColumn, AlterTable
from database.ddl_base.ddl_leafs import ShowColumns, ColumnNotNull, ColumnDefault, Leaf, AddColumn


def test_line_translate(default_translator, column):
    alter_table = AlterTable('users')
    alter_column = AlterColumn(column)

    assert default_translator.translate(alter_table) == 'ALTER TABLE users'
    assert default_translator.translate(alter_column) == 'ALTER COLUMN password'
    assert default_translator.translate(Composite()) == ''


def test_default_translate_leafs(default_translator, column):
    not_null = ColumnNotNull()
    default = ColumnDefault('xd')

    assert default_translator.translate(not_null) == 'SET NOT NULL'
    assert default_translator.translate(default) == "SET DEFAULT xd"
    assert default_translator.translate(ShowColumns('users')) == 'SHOW COLUMNS FROM users'
    assert default_translator.translate(Leaf()) == ''

