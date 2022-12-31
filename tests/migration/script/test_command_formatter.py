from migration.script.command_formatter import CommandFormatter, split_arguments_by_commas, \
    split_command_by_name_and_brackets


def test_command_formatter_brackets():
    command = 'ShowColumn("users")'
    assert CommandFormatter.format_command(command) == ['ShowColumn("users")']


def test_command_formatter_command():
    command = 'AlterColumn("users", "id", ColumnNotNull())'
    assert CommandFormatter.format_command(command) == ['AlterColumn("users", "id", ColumnNotNull())']


def test_command_formatter_command_with_brackets():
    command = 'AlterColumn("users", "id", ColumnNotNull(), ColumnDefault("xd"))'
    assert CommandFormatter.format_command(command) == ['AlterColumn("users", "id", ',
                                                        'ColumnNotNull(), ',
                                                        'ColumnDefault("xd"))']


def test_command_formatter_command_with_brackets_and_long_name():
    command = 'AlterColumn("users", "id", "ColumnNotNull", "ColumnDefault", "ShowColumns_users")'
    assert CommandFormatter.format_command(command) == ['AlterColumn("users", "id", "ColumnNotNull", "ColumnDefault", ',
                                                        '"ShowColumns_users")']


def test_divide_commands_by_commas():
    command = '"users", "id", 3, "xd"'
    assert split_arguments_by_commas(command) == ['"users"', '"id"', '3', '"xd"']

    command = '"users", "id", ColumnNotNull(), ColumnDefault("xd")'
    assert split_arguments_by_commas(command) == ['"users"', '"id"', 'ColumnNotNull()',
                                                  'ColumnDefault("xd")']

    command = 'AlterColumn("users", "id", ColumnNotNull(), ColumnDefault("xd")), ShowColumns("users")'
    assert split_arguments_by_commas(command) == ['AlterColumn("users", "id", ColumnNotNull(), ColumnDefault("xd"))',
                                                  'ShowColumns("users")']


def test_split_command_by_name_and_brackets():
    command = 'AlterColumn("users", "id", ColumnNotNull(), ColumnDefault("xd"))'
    assert split_command_by_name_and_brackets(command) == ['AlterColumn(',
                                                           '"users", "id", ColumnNotNull(), '
                                                           'ColumnDefault("xd")', ')']
