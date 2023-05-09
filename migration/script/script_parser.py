import os

from database.ddl_base.ddl_components_abstract import DDLComponent
from database.ddl_base.ddl_composites import *
from database.ddl_base.ddl_leafs import *


class ScriptParser:
    """
    Class for parsing script to DDLComponent
    """

    def _create_file(self):
        dir_name = os.path.dirname(self.script_path)
        os.makedirs(dir_name, exist_ok=True)

    def __init__(self, script_name: str, script_path: str):
        """
        Constructor for ScriptParser

        Args:
            script_name: name of script
            script_path: path to script
        """

        self.script_name = script_name
        self.script_path = script_path
        self._create_file()
        self._script_file = open(self.script_path, 'r')

    def get_script(self) -> str:
        """
        Get script from file

        Returns:
            script as List of strings
        """

        lines = self._script_file.readlines()

        for i in range(len(lines)):
            if 'upgrade' in lines[i]:
                return "".join(lines[i+2:])

    def close(self) -> None:
        """
        Close script file
        """

        self._script_file.close()

    @staticmethod
    def parse_script(script: str) -> DDLComponent:
        """
        Parses script to DDLComponent

        Args:
            script: script to parse as string

        Returns:
            DDLComponent as Composite
        """

        script_parts = script.replace(' ', '').split('\n')

        for i in range(len(script_parts)):
            if len(script_parts[i]) > 0 and script_parts[i][-1] != ',':
                script_parts[i] += ','

        composite_script = "Composite(" + "".join(script_parts) + ")"

        return eval(composite_script)
