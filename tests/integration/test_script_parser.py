from migration.script.script_parser import ScriptParser

dir_ = 'tests/integration/true_files'
script_name = 'test_script.py'
script_path = dir_ + '/' + script_name


def test_get_script():
    script_builder = ScriptParser(script_name, script_path)

    result = script_builder.get_script()
    script_builder.close()

    assert result is not None
    assert len(result) > 0
    assert result == '''    AlterTable('users', False,
               AlterColumn(Column('password', 'VARCHAR(40)', False, None, None, None, None),
                           ColumnNotNull(True),
                           ColumnDefault('xd')))
    ShowColumns('users')
'''
