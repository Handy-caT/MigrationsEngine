from migration.script.script_builder.import_formatter import get_import_dict, ImportFormatter


def test_get_import_dict():
    command = ['AlterTable', 'AlterColumn', 'ColumnDefault', 'ColumnNotNull', 'ShowColumns']
    import_lists_dict = get_import_dict(command)
    assert import_lists_dict == {'database.ddl_base.ddl_composites': ['AlterTable', 'AlterColumn'],
                                 'database.ddl_base.ddl_leafs': ['ColumnDefault', 'ColumnNotNull', 'ShowColumns']}


def test_format_imports():
    commands = ['AlterColumn("users", "id", "ColumnNotNull", "ColumnDefault",',
                '"ShowColumns_users",',
                'ColumnNotNull(),',
                'ColumnDefault("xd"))']

    assert ImportFormatter.format_imports(commands) == ['from database.ddl_base.ddl_composites import AlterColumn',
                                                        'from database.ddl_base.ddl_leafs import ColumnNotNull, '
                                                        'ColumnDefault']
