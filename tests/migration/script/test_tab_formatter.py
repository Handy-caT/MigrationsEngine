from migration.script.tab_formatter import TabFormatter


def test_add_tabs():
    command = ['AlterColumn("users", "id", ColumnNotNull(), ColumnDefault("xd"))']
    assert TabFormatter.add_tabs(command, 1) == ['    AlterColumn("users", "id", ColumnNotNull(), ColumnDefault("xd"))']

    command = ['FirstLine', 'SecondLine']
    assert TabFormatter.add_tabs(command, 1) == ['    FirstLine', '    SecondLine']

    command = ['FirstLine', 'SecondLine']
    assert TabFormatter.add_tabs(command, 2) == ['        FirstLine', '        SecondLine']

    command = ['  FirstLine', ' SecondLine  ']
    assert TabFormatter.add_tabs(command, 1) == ['    FirstLine', '    SecondLine']


def test_add_spaces():
    command = ['AlterColumn("users", "id", ColumnNotNull(), ColumnDefault("xd"))']
    assert TabFormatter.add_spaces(command, 1) == [' AlterColumn("users", "id", ColumnNotNull(), ColumnDefault("xd"))']

    command = ['FirstLine', 'SecondLine']
    assert TabFormatter.add_spaces(command, 1) == [' FirstLine', ' SecondLine']

    command = ['FirstLine', 'SecondLine']
    assert TabFormatter.add_spaces(command, 2) == ['  FirstLine', '  SecondLine']

    command = ['  FirstLine', ' SecondLine  ']
    assert TabFormatter.add_spaces(command, 1) == [' FirstLine', ' SecondLine']


def test_format_command():
    command = ['AlterColumn("users", "id",', 'ColumnNotNull(),', 'ColumnDefault("xd"))']
    length = len('AlterColumn(')
    assert TabFormatter.format_command(command) == ['AlterColumn("users", "id",',
                                                    ' ' * length + 'ColumnNotNull(),',
                                                    ' ' * length + 'ColumnDefault("xd"))']


def test_format_command2():
    command = ['AlterColumn("users", "id",', 'Command("parameter",', 'SubCommand1(),', 'SubCommand2("parameter")),',
               'ColumnDefault("xd"))']
    length = len('AlterColumn(')
    length2 = len('Command(') + length
    assert TabFormatter.format_command(command) == ['AlterColumn("users", "id",',
                                                    ' ' * length + 'Command("parameter",',
                                                    ' ' * length2 + 'SubCommand1(),',
                                                    ' ' * length2 + 'SubCommand2("parameter")),',
                                                    ' ' * length + 'ColumnDefault("xd"))']
