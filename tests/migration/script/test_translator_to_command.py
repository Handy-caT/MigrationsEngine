from migration.script.translator_to_command import TranslatorToCommand


def test_translate_composite(composite_ddl):
    translator = TranslatorToCommand()

    result = translator.translate(composite_ddl)

    assert result == ["AlterTable('users', False,",
                      "           AlterColumn(Column('password', 'VARCHAR(40)', False, None, None, None, None),",
                      '                       ColumnNotNull(True),',
                      "                       ColumnDefault('xd')))",
                      "ShowColumns('users')"]


def test_translate_alter_table(composite_ddl):
    translator = TranslatorToCommand()

    result = translator.translate(composite_ddl.components[0])

    assert result == ["AlterTable('users', False,",
                      "           AlterColumn(Column('password', 'VARCHAR(40)', False, None, None, None, None),",
                      '                       ColumnNotNull(True),',
                      "                       ColumnDefault('xd')))"]


def test_translate_easy_command(composite_ddl):
    translator = TranslatorToCommand()

    result = translator.translate(composite_ddl.components[1])

    assert result == ["ShowColumns('users')"]


def test_get_command(composite_ddl):
    translator = TranslatorToCommand()

    result = translator.translate(composite_ddl)

    assert translator.get_command(result) == "AlterTable('users', False,\n" \
                                             "           AlterColumn(Column('password', 'VARCHAR(40)'," \
                                             " False, None, None, None, None),\n" \
                                             '                       ColumnNotNull(True),\n' \
                                             "                       ColumnDefault('xd')))\n" \
                                             "ShowColumns('users')"
