from typing import List

from database.ddl_base.ddl_components_abstract import DDLComponent
from database.ddl_base.ddl_composites import Composite
from database.translator import Translator
from migration.script.command_formatter import CommandFormatter
from migration.script.script_builder.tab_formatter import TabFormatter


class TranslatorToCommand(Translator):
    """
    Class for translating DDLComponent to command as a List of strings
    """

    def __init__(self, dialect: str = 'command'):
        super().__init__({}, dialect)

    def _translate_composite(self, component: Composite) -> List[str]:
        result = []
        for component in component.components:
            result.extend(self.translate(component))

        return result

    def translate(self, component: DDLComponent) -> List[str]:
        """
        Translates DDLComponent to command as a List of strings

        Args:
            component: DDLComponent to translate

        Returns:
            command as a List of strings
        """

        if isinstance(component, Composite):
            return self._translate_composite(component)
        else:
            represent = component.__repr__()
            formatted_command = CommandFormatter.format_command(represent)
            result = TabFormatter.format_command(formatted_command)

            return result

    @staticmethod
    def get_command(command: List[str]) -> str:
        """
        Creates a string command from multiline List of strings

        Args:
            command: multiline List of strings

        Returns:
            command as a string
        """

        return '\n'.join(command).strip()
