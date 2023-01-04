from migration.script.command_formatter import command_start

_tab = '    '
_space = ' '


class TabFormatter:
    @staticmethod
    def add_tabs(command: list[str], tabs: int) -> list[str]:
        result = []
        for line in command:
            result.append(_tab * tabs + line.strip())
        return result

    @staticmethod
    def add_spaces(command: list[str], space: int) -> list[str]:
        result = []
        for line in command:
            result.append(_space * space + line.strip())
        return result

    @staticmethod
    def format_command(command: list[str]) -> list[str]:
        result = [command[0]]
        space_len = len(command_start(command[0]))
        last_space_len = space_len

        for i in range(1, len(command)):
            result.append(_space * space_len + command[i].strip())

            if command[i].count('(') > command[i].count(')'):
                last_space_len = len(command_start(command[i]))
                space_len += last_space_len
            elif command[i].count('(') < command[i].count(')'):
                space_len -= last_space_len
                last_space_len = 0
            else:
                pass

        return result
