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
from database.ddl_base.ddl_composites import AlterTable, AlterColumn, Composite
from database.ddl_base.ddl_leafs import RenameColumn, ColumnNotNull, ColumnDefault, ShowColumns
from database.translator import DefaultTranslator

#temp = '%s %s'
#print(temp % ('hello', 'xd'))

table = AlterTable('users')
column = AlterColumn('data')
column.add_component(ColumnNotNull())
column.add_component(ColumnDefault('xd'))
table.add_component(column)
table.add_component(RenameColumn('old_name', 'new_name'))

composite = Composite()
composite.add_component(table)
composite.add_component(ShowColumns('users'))

for i in composite:
    print(i)

translator = DefaultTranslator()
res = translator.translate(composite)
print(res)
