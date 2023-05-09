from database.ddl_base.ddl_components_abstract import DDLComponent
from migration.script.script_builder.script_builder import ScriptBuilder
from migration.script.script_parser import ScriptParser
from migration.script.translator_to_command import TranslatorToCommand


class ScriptFacade:
    """
    Facade for ScriptBuilder and ScriptParser

    Attributes:
        script_name: name of script
        script_path: path to script
    """

    def __init__(self, script_name, script_path):
        """
        Constructor for ScriptFacade

        Args:
            script_name: name of script
            script_path: path to script
        """

        self.script_name = script_name
        self.script_path = script_path
        self._translator = TranslatorToCommand()

    def create_script(self, component: DDLComponent) -> None:
        """
        Creates script from DDLComponent on path specified in constructor

        Args:
            component: DDLComponent to create script from
        """

        translated = self._translator.translate(component)
        script_builder = ScriptBuilder(self.script_name, self.script_path)

        script_builder.build_info()
        script_builder.build_imports(translated)
        script_builder.build_upgrade()
        script_builder.build_command(translated)
        script_builder.close()

    def parse_script(self) -> DDLComponent:
        """
        Parses script to DDLComponent from path specified in constructor

        Returns:
            DDLComponent as Composite
        """

        script_parser = ScriptParser(self.script_name, self.script_path)

        script = script_parser.get_script()
        script_parser.close()

        component = ScriptParser.parse_script(script)

        return component
