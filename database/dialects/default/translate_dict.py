from database.ddl_base.ddl_composites import AlterTable, AlterColumn, Composite
from database.ddl_base.ddl_leafs import ColumnDefault, ColumnNotNull, DropColumn, RenameColumn, ShowColumns, Leaf, \
    DropConstraint, ColumnUnique, AddColumn, DropDefault


def _alter_table(component: AlterTable) -> str:
    if component.if_exists:
        return 'ALTER TABLE IF EXISTS %s' % component.table_name
    else:
        return 'ALTER TABLE %s' % component.table_name


def _column_unique(component: ColumnUnique) -> str:
    columns = ''
    if len(component.unique.columns) > 1:
        for column in component.unique.columns:
            columns += column + ', '
    else:
        columns = component.unique.columns[0]

    return 'ADD CONSTRAINT %s UNIQUE (%s)' % (component.unique.name,columns)


def _add_column(component: AddColumn) -> str:
    command = 'ADD COLUMN %s %s' % (component.column.name, component.column.column_type)
    if component.column.not_null:
        command += ' NOT NULL'

    if component.column.default:
        command += ' DEFAULT %s' % component.column.default

    return command


translate_dict_default = {
    AlterTable.__name__: _alter_table,
    AlterColumn.__name__: (lambda component: 'ALTER COLUMN %s' % component.column.name),
    ColumnDefault.__name__: (lambda component: 'SET DEFAULT %s' % component.default),
    ColumnNotNull.__name__: (lambda component: 'SET NOT NULL'),
    DropColumn.__name__: (lambda component: 'DROP COLUMN %s' % component.column_name),
    DropDefault.__name__: (lambda component: 'DROP DEFAULT'),
    RenameColumn.__name__: (lambda component: 'RENAME COLUMN %s TO %s' % (component.old_name,
                                                                          component.new_name)),
    ShowColumns.__name__: (lambda component: 'SHOW COLUMNS FROM %s' % component.table_name),
    DropConstraint.__name__: (lambda component: 'DROP CONSTRAINT %s' % component.constraint_name),
    AddColumn.__name__: _add_column,
    ColumnUnique.__name__: _column_unique,
    Composite.__name__: (lambda component: ''),
    Leaf.__name__: (lambda component: ''),
}
