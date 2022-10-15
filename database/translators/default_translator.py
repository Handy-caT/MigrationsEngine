from database.abstract_translator import AbstractTranslator
from database.ddl_base.ddl_components_abstract import DDLComponent
from database.ddl_base.ddl_composites import AlterTable, AlterColumn
from database.ddl_base.ddl_leafs import ColumnDefault, ColumnNotNull, RenameColumn, DropColumn


def _alter_table(component: AlterTable) -> str:
    if component.if_exists:
        return 'ALTER TABLE IF EXISTS %s' % component.table_name
    else:
        return 'ALTER TABLE %s' % component.table_name


def _alter_column(component: AlterColumn) -> str:
    return 'ALTER COLUMN %s' % component.column_name


def _column_default(component: ColumnDefault) -> str:
    return 'SET DEFAULT %s' % component.default


def _column_not_null(component: ColumnNotNull) -> str:
    return 'SET NOT NULL'


def _rename_column(component: RenameColumn) -> str:
    return 'RENAME COLUMN %s TO %s' % (component.old_name, component.new_name)


def _drop_column(component: DropColumn) -> str:
    return 'DROP COLUMN %s' % component.column_name


translate_dict = {
    'AlterTable': _alter_table,
    'AlterColumn': _alter_column,
    'ColumnDefault': _column_default,
    'ColumnNotNull': _column_not_null,
    'DropColumn': _drop_column,
    'RenameColumn': _rename_column,
}


def _translate_one(component: DDLComponent):
    return translate_dict[component.__class__.__name__](component)


def _get_command(command: list[str]) -> str:
    return ' '.join(command) + ';'


class DefaultTranslator(AbstractTranslator):
    @property
    def dialect(self):
        return 'default'

    def translate(self, ddl_component: DDLComponent):
        command = []
        depth = 0
        result = []

        for i in ddl_component:
            if i[1] > depth:
                depth += 1
            else:
                while len(command) > i[1]:
                    command.pop()

            if i[0].is_composite:
                command.append(_translate_one(i[0]))
            else:
                command.append(_translate_one(i[0]))
                result.append(_get_command(command))

        return result
