import re

class_with_inner_brackets = re.compile(r'([A-Z][a-zA-Z]*\()(.*)(\))')
class_without_inner_brackets = re.compile(r'([A-Z][a-zA-Z]*\()([^()]*)(\))')


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
            return [command]
