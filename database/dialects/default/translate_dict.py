from database.ddl_base.ddl_composites import AlterTable


def _alter_table(component: AlterTable) -> str:
    if component.if_exists:
        return 'ALTER TABLE IF EXISTS %s' % component.table_name
    else:
        return 'ALTER TABLE %s' % component.table_name


translate_dict_default = {
    'AlterTable': _alter_table,
    'AlterColumn': (lambda component: 'ALTER COLUMN %s' % component.column_name),
    'ColumnDefault': (lambda component: 'SET DEFAULT %s' % component.default),
    'ColumnNotNull': (lambda component: 'SET NOT NULL'),
    'DropColumn': (lambda component: 'DROP COLUMN %s' % component.column_name),
    'RenameColumn': (lambda component: 'RENAME COLUMN %s TO %s' % (component.old_name, component.new_name)),
    'ShowColumns': (lambda component: 'SHOW COLUMNS FROM %s' % component.table_name),
    'Composite': (lambda component: '')
}
