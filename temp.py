# column = Column('data', String(40), ForeignKey('users.id'), autoincrement=True)
#
# for i in column.foreign_keys:
#     print(i.target_fullname)
#
# print(column.key)
#
# print(column.type)
#
# print(column.default)
from copy import deepcopy

from database.ddl_base.ddl_composites import AlterTable, AlterColumn, Composite
from database.ddl_base.ddl_leafs import RenameColumn, ColumnNotNull, ColumnDefault, ShowColumns
from database.dialects.mysql.mysql_visitor import MySqlVisitor
from database.dialects.mysql.translate_dict import translate_dict_mysql
from database.translator import Translator
from database.schema.column import Column

#temp = '%s %s'
#print(temp % ('hello', 'xd'))

column_obj = Column(
        name='password',
        column_type='varchar(40)',
        not_null=False,
        key=None,
        default=None,
        extra=None
    )

table = AlterTable('users')
column = AlterColumn(column_obj)
column.add_component(ColumnNotNull())
column.add_component(ColumnDefault('xd'))
table.add_component(column)
table.add_component(RenameColumn('old_name', 'new_name'))

composite = Composite()
composite.add_component(table)
composite.add_component(ShowColumns('users'))

# visitor = MySqlVisitor()
#
# for i in composite:
#     i.accept(visitor)
#     print(f'#{i}')
#
# translator = Translator(translate_dict_mysql)
# print(translator.translate(table))

