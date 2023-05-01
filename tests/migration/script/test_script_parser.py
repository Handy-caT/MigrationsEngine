from migration.script.script_parser import ScriptParser


def test_parse_script(composite_ddl):
    script = '''AlterTable('users', False,
                AlterColumn(Column('password', 'VARCHAR(40)', False, None, None, None, None),
                           ColumnNotNull(True),
                           ColumnDefault('xd')))
    ShowColumns('users')
    '''

    new_composite = ScriptParser.parse_script(script)

    assert new_composite.is_composite
    assert new_composite == composite_ddl
