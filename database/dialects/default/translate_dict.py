from database.ddl_base.ddl_composites import AlterTable, AlterColumn, Composite
from database.ddl_base.ddl_leafs import ColumnDefault, ColumnNotNull, DropColumn, RenameColumn, ShowColumns, Leaf, \
    DropConstraint, ColumnUnique, AddColumn, DropDefault


def _alter_table(component: AlterTable) -> str:
    if component.if_exists:
        return f'ALTER TABLE IF EXISTS {component.table_name}'
    else:
        return f'ALTER TABLE {component.table_name}'


def _column_unique(component: ColumnUnique) -> str:
    columns = ''
    if len(component.unique.columns) > 1:
        for column in component.unique.columns:
            columns += column + ', '
    else:
        columns = component.unique.columns[0]

    return f'ADD CONSTRAINT {component.unique.name} UNIQUE ({columns})'


def _add_column(component: AddColumn) -> str:
    command = f'ADD COLUMN {component.column.name} {component.column.column_type}'
    if component.column.not_null:
        command += ' NOT NULL'

    if component.column.default:
        command += f' DEFAULT {component.column.default}'

    return command


translate_dict_default = {
    AlterTable.__name__: _alter_table,
    AlterColumn.__name__: (lambda component: f'ALTER COLUMN {component.column.name}'),
    ColumnDefault.__name__: (lambda component: f'SET DEFAULT {component.default}'),
    ColumnNotNull.__name__: (lambda component: 'SET NOT NULL'),
    DropColumn.__name__: (lambda component: f'DROP COLUMN {component.column_name}'),
    DropDefault.__name__: (lambda component: 'DROP DEFAULT'),
    RenameColumn.__name__: (lambda component: f'RENAME COLUMN {component.old_name}'
                                              f' TO {component.new_name}'),
    ShowColumns.__name__: (lambda component: f'SHOW COLUMNS FROM {component.table_name}'),
    DropConstraint.__name__: (lambda component: f'DROP CONSTRAINT {component.constraint_name}'),
    AddColumn.__name__: _add_column,
    ColumnUnique.__name__: _column_unique,
    Composite.__name__: (lambda component: ''),
    Leaf.__name__: (lambda component: ''),
}
