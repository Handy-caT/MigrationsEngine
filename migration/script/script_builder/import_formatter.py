from typing import List
import re

from database.ddl_base.ddl_composites import AlterColumn, AlterTable, Composite
from database.ddl_base.ddl_leafs import ColumnDefault, ColumnNotNull, DropColumn, DropDefault, RenameColumn, \
    ShowColumns, DropConstraint, AddColumn, ColumnUnique, Leaf
from database.dialects.mysql.mysql_ddl import NotNull, Default, ModifyColumn
from database.schema.column import Column

class_start = re.compile(r'([A-Z][a-zA-Z1-9]*)(\()')

import_dict = {
    AlterColumn.__name__: 'database.ddl_base.ddl_composites',
    AlterTable.__name__: 'database.ddl_base.ddl_composites',
    ColumnDefault.__name__: 'database.ddl_base.ddl_leafs',
    ColumnNotNull.__name__: 'database.ddl_base.ddl_leafs',
    DropColumn.__name__: 'database.ddl_base.ddl_leafs',
    DropDefault.__name__: 'database.ddl_base.ddl_leafs',
    RenameColumn.__name__: 'database.ddl_base.ddl_leafs',
    ShowColumns.__name__: 'database.ddl_base.ddl_leafs',
    DropConstraint.__name__: 'database.ddl_base.ddl_leafs',
    AddColumn.__name__: 'database.ddl_base.ddl_leafs',
    ColumnUnique.__name__: 'database.ddl_base.ddl_leafs',
    Composite.__name__: 'database.ddl_base.ddl_composites',
    Leaf.__name__: 'database.ddl_base.ddl_leafs',
    NotNull.__name__: 'database.dialects.mysql.mysql_ddl',
    Default.__name__: 'database.dialects.mysql.mysql_ddl',
    ModifyColumn.__name__: 'database.dialects.mysql.mysql_ddl',
    Column.__name__: 'database.schema.column',
}


def get_import_dict(commands: List[str]) -> dict:
    import_lists_dict = {}
    for item in commands:
        from_ = import_dict[item]
        if from_ not in import_lists_dict:
            import_lists_dict[from_] = [item]
        else:
            import_lists_dict[from_].append(item)

    return import_lists_dict


class ImportFormatter:
    @staticmethod
    def format_imports(command: List[str]) -> List[str]:
        imports = []
        for line in command:
            command = re.findall(class_start, line)
            if command:
                for i in command:
                    if i[0] not in imports and i[0] in import_dict:
                        imports.append(i[0])

        import_lists_dict = get_import_dict(imports)
        result = []
        for key, value in import_lists_dict.items():
            result.append(f'from {key} import {", ".join(value)}')

        return result
