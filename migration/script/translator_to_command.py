from database.ddl_base.ddl_components_abstract import DDLComponent
from database.ddl_base.ddl_composites import Composite
from database.translator import Translator
from migration.script.command_formatter import CommandFormatter
from migration.script.tab_formatter import TabFormatter


class TranslatorToCommand(Translator):
    def __init__(self, dialect: str = 'command'):
        super().__init__({}, dialect)

    def _translate_composite(self, component: Composite) -> list[str]:
        result = []
        for component in component.components:
            result.extend(self.translate(component))

        return result

    def translate(self, component: DDLComponent) -> list[str]:
        if isinstance(component, Composite):
            return self._translate_composite(component)
        else:
            represent = component.__repr__()
            formatted_command = CommandFormatter.format_command(represent)
            result = TabFormatter.format_command(formatted_command)

            return result

    @staticmethod
    def get_command(command: list[str]) -> str:
        raise NotImplementedError
