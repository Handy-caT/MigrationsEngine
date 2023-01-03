import re

class_with_inner_brackets = re.compile(r'([A-Z][a-zA-Z]*\()(.*)(\))')
class_without_inner_brackets = re.compile(r'([A-Z][a-zA-Z]*\()([^()]*)(\))')


def is_command(command: str) -> bool:
    matches = re.search(class_with_inner_brackets, command)
    if matches:
        return True
    else:
        return False


def split_arguments_by_commas(command: str) -> list[str]:
    parts = command.split(',')
    parts = [part.strip() for part in parts]

    i = 0
    while i < len(parts):
        if parts[i].count('(') > parts[i].count(')'):
            parts[i] += ', ' + parts[i + 1]
            parts.pop(i + 1)
        else:
            i += 1

    return parts


def split_command_by_name_and_brackets(command: str) -> list[str]:
    matches = re.search(class_with_inner_brackets, command)
    if matches:
        return [matches.group(1), matches.group(2), matches.group(3)]
    else:
        matches = re.search(class_without_inner_brackets, command)
        return [matches.group(1), matches.group(2), matches.group(3)]


def long_arguments_formatter(command: str) -> list[str]:
    if len(command) > 79:
        splitted = split_command_by_name_and_brackets(command)
        result = [splitted[0]]
        splitted_arguments = split_arguments_by_commas(splitted[1])

        result[-1] += splitted_arguments[0]

        for i in range(1, len(splitted_arguments)):
            if len(splitted_arguments[i]) + len(result[-1]) + 2 > 79:
                result[-1] += ', '
                result.append(splitted_arguments[i])
            else:
                result[-1] += ', ' + splitted_arguments[i]

        result[-1] += ')'

        return result
    else:
        return [command]


def format_command_with_inner_brackets(command: str) -> list[str]:
    result = []

    matches = re.search(class_with_inner_brackets, command)
    result.append(matches.group(1))

    inner_part = matches.group(2)
    splitted_inner_part = split_arguments_by_commas(inner_part)

    next_line = splitted_inner_part[0]
    for i in range(1, len(splitted_inner_part)):
        if not is_command(splitted_inner_part[i]):
            next_line += ', ' + splitted_inner_part[i]
        else:
            if next_line != "":
                result.append(next_line + ',')
                next_line = ""
            result.append(splitted_inner_part[i] + ',')

    result[0] += result[1]
    result.pop(1)

    if is_command(splitted_inner_part[-1]):
        result[-1] = result[-1][:-1]

    result[-1] += ')'

    return result


class CommandFormatter:

    @staticmethod
    def format_command(command: str) -> list[str]:
        brackets = command.count('(')
        if brackets > 2:
            return format_command_with_inner_brackets(command)
        else:
            return long_arguments_formatter(command)
