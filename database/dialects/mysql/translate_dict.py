from database.dialects.default.translate_dict import translate_dict_default
from database.dialects.mysql.mysql_ddl import NotNull, Default, ModifyColumn


def _not_null(component: NotNull) -> str:
    if component.not_null:
        return 'NOT NULL'
    return 'NULL'


translate_dict_mysql = {
    **translate_dict_default,
    NotNull.__name__: _not_null,
    Default.__name__: (lambda component: 'DEFAULT %s' % component.default),
    ModifyColumn.__name__: (lambda component: 'MODIFY COLUMN %s %s' % (component.column.name,
                                                                       component.column.column_type)),
}
