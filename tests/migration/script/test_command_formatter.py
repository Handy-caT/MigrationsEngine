from migration.script.command_formatter import CommandFormatter


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
