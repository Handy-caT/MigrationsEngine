import os.path
from typing import List

from migration.script.script_builder.script_templates import get_info, get_upgrade_template
from migration.script.tab_formatter import TabFormatter


class ScriptBuilder:
    def _create_file(self):
        dir_name = os.path.dirname(self.script_path)
        os.makedirs(dir_name, exist_ok=True)

    def __init__(self, script_name, script_path):
        self.script_name = script_name
        self.script_path = script_path
        self._create_file()
        self.script_file = open(self.script_path, 'w')

    def build_info(self) -> None:
        info = get_info(self.script_name)
        self.script_file.write(info + '\n')

    def build_upgrade(self) -> None:
        upgrade = get_upgrade_template()
        self.script_file.write(upgrade + '\n')

    def build_command(self, command: List[str]) -> None:
        command = TabFormatter.add_tabs(command, 1)

        for line in command:
            self.script_file.write(line + '\n')

    def close(self) -> None:
        self.script_file.close()
        