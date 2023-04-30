from database.ddl_base.ddl_components_abstract import DDLComponent
from database.ddl_base.ddl_composites import *
from database.ddl_base.ddl_leafs import *


class ScriptParser:

    @staticmethod
    def parse_script(script: str) -> DDLComponent:
        script_parts = script.replace(' ', '').split('\n')

        for i in range(len(script_parts)):
            if len(script_parts[i]) > 0 and script_parts[i][-1] != ',':
                script_parts[i] += ','

        composite_script = "Composite(" + "".join(script_parts) + ")"

        return eval(composite_script)
