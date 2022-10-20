from database.dialects.default.translate_dict import translate_dict_default
from database.dialects.mysql.mysql_ddl import NotNull


def _not_null(component: NotNull) -> str:
    if component.not_null:
        return 'NOT NULL'
    else:
        return 'NULL'


translate_dict_mysql = {
    'AlterTable': translate_dict_default['AlterTable'],
    'AlterColumn': translate_dict_default['AlterColumn'],
    'ColumnDefault': translate_dict_default['ColumnDefault'],
    'ColumnNotNull': translate_dict_default['ColumnNotNull'],
    'NotNull': _not_null,
    'Default': (lambda component: 'DEFAULT %s' % component.default),
    'ModifyColumn': (lambda component: 'MODIFY COLUMN %s %s' % (component.column.name, component.column.column_type)),
    'RenameColumn': translate_dict_default['RenameColumn'],
    'Leaf': translate_dict_default['Leaf'],
}
