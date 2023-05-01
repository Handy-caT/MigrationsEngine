from database.ddl_base.ddl_components_abstract import DDLComponent
from database.ddl_base.ddl_composites import *
from database.ddl_base.ddl_leafs import *


class ScriptParser:
    """
    Class for parsing script to DDLComponent
    """

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
