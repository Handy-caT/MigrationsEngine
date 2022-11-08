from database.ddl_base.ddl_composites import AlterTable, AlterColumn, Composite
from database.ddl_base.ddl_leafs import ColumnDefault, ColumnNotNull, DropColumn, RenameColumn, ShowColumns, Leaf


def _alter_table(component: AlterTable) -> str:
    if component.if_exists:
        return 'ALTER TABLE IF EXISTS %s' % component.table_name
    else:
        return 'ALTER TABLE %s' % component.table_name


translate_dict_default = {
    AlterTable.__name__: _alter_table,
    AlterColumn.__name__: (lambda component: 'ALTER COLUMN %s' % component.column.name),
    ColumnDefault.__name__: (lambda component: 'SET DEFAULT %s' % component.default),
    ColumnNotNull.__name__: (lambda component: 'SET NOT NULL'),
    DropColumn.__name__: (lambda component: 'DROP COLUMN %s' % component.column_name),
    RenameColumn.__name__: (lambda component: 'RENAME COLUMN %s TO %s' % (component.old_name, component.new_name)),
    ShowColumns.__name__: (lambda component: 'SHOW COLUMNS FROM %s' % component.table_name),
    Composite.__name__: (lambda component: ''),
    Leaf.__name__: (lambda component: ''),
}
