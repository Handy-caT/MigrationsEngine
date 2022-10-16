from database.abstract_translator import AbstractTranslator
from database.ddl_base.ddl_components_abstract import DDLComponent
from database.ddl_base.ddl_composites import AlterTable


def _alter_table(component: AlterTable) -> str:
    if component.if_exists:
        return 'ALTER TABLE IF EXISTS %s' % component.table_name
    else:
        return 'ALTER TABLE %s' % component.table_name


translate_dict = {
    'AlterTable': _alter_table,
    'AlterColumn': (lambda component: 'ALTER COLUMN %s' % component.column_name),
    'ColumnDefault': (lambda component: 'SET DEFAULT %s' % component.default),
    'ColumnNotNull': (lambda component: 'SET NOT NULL'),
    'DropColumn': (lambda component: 'DROP COLUMN %s' % component.column_name),
    'RenameColumn': (lambda component: 'RENAME COLUMN %s TO %s' % (component.old_name, component.new_name)),
    'ShowColumns': (lambda component: 'SHOW COLUMNS FROM %s' % component.table_name),
    'Composite': (lambda component: '')
}


def _translate_one(component: DDLComponent):
    return translate_dict[component.__class__.__name__](component)


def _get_command(command: list[str]) -> str:
    return (' '.join(command) + ';').lstrip()


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
