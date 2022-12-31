import re

class_with_inner_brackets = re.compile(r'([A-Z][a-zA-Z]*\()(.*)(\))')
class_without_inner_brackets = re.compile(r'([A-Z][a-zA-Z]*\()([^()]*)(\))')


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


class CommandFormatter:
    @staticmethod
    def _format_command_brackets(command: str) -> list[str]:
        result = []

        matches = re.search(class_with_inner_brackets, command)
        result.append(matches.group(1))

        inner_part = matches.group(2)
        matches = re.findall(class_without_inner_brackets, inner_part)
        if len(matches) > 1:
            splitted = inner_part.split(', ')
            for i in splitted:
                if re.fullmatch(class_without_inner_brackets, i):
                    result.append(i + ', ')
                else:
                    result[0] += i + ', '
            result[-1] = result[-1][:-2]
            result[-1] += ')'
        else:
            result[0] += inner_part + ')'

        return result

    @staticmethod
    def format_command(command: str) -> list[str]:
        brackets = command.count('(')
        if brackets > 2:
            return CommandFormatter._format_command_brackets(command)
        else:
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
