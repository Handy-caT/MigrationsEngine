from migration.script.command_formatter import CommandFormatter, split_arguments_by_commas, \
    split_command_by_name_and_brackets, has_command, command_start


def test_command_formatter_brackets():
    command = 'ShowColumn("users")'
    assert CommandFormatter.format_command(command) == ['ShowColumn("users")']


def test_command_formatter_command_one_command_argument():
    command = 'AlterColumn("users", "id", ColumnNotNull())'
    assert CommandFormatter.format_command(command) == ['AlterColumn("users", "id", ColumnNotNull())']


def test_command_formatter_command_with_brackets():
    command = 'AlterColumn("users", "id", ColumnNotNull(), ColumnDefault("xd"))'
    assert CommandFormatter.format_command(command) == ['AlterColumn("users", "id",',
                                                        'ColumnNotNull(),',
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


def test_is_command():
    command = 'AlterColumn("users", "id", ColumnNotNull(), ColumnDefault("xd"))'
    assert has_command(command) is True

    command = 'ShowColumn("users")'
    assert has_command(command) is True

    command = '"users"'
    assert has_command(command) is False

    command = 'SubCommand1()'
    assert has_command(command) is True


def test_split_long_command_format():
    command = 'AlterColumn("users", "id", "ColumnNotNull", "ColumnDefault", "ShowColumns_users", ' \
              ' ColumnNotNull(), ColumnDefault("xd"))'
    assert CommandFormatter.format_command(command) == ['AlterColumn("users", "id", "ColumnNotNull", "ColumnDefault",',
                                                        '"ShowColumns_users",',
                                                        'ColumnNotNull(),',
                                                        'ColumnDefault("xd"))']


def test_split_long_command_format_with_long_arguments():
    command = 'AlterColumn("users", "id", "ColumnNotNull", "ColumnDefault", "ShowColumns_users", ' \
              ' Command("parameter1", "parameter2", SubCommand1(), SubCommand2("parameter")), ColumnDefault("xd"))'
    assert CommandFormatter.format_command(command) == ['AlterColumn("users", "id", "ColumnNotNull", "ColumnDefault",',
                                                        '"ShowColumns_users",',
                                                        'Command("parameter1", "parameter2",',
                                                        'SubCommand1(),',
                                                        'SubCommand2("parameter")),',
                                                        'ColumnDefault("xd"))']


def test_class_start():
    command = 'AlterColumn("users", "id", ColumnNotNull(), ColumnDefault("xd"))'
    assert command_start(command) == 'AlterColumn('

    command = 'ShowColumn("users")'
    assert command_start(command) == 'ShowColumn('
