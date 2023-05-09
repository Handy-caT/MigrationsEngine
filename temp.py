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
import re
from os import mkdir

from database.ddl_base.ddl_composites import AlterTable, AlterColumn, Composite
from database.ddl_base.ddl_leafs import RenameColumn, ColumnNotNull, ColumnDefault, ShowColumns
from database.schema.column import Column
from migration.script.script_builder.script_templates import get_info

# temp = '%s %s'
# print(temp % ('hello', 'xd'))

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

# print(composite.__repr__())
# import re
# regex = r'([A-Z][a-zA-Z]*\()(.*)(\))'
# regex2 = r'([A-Z][a-zA-Z]*\()([^()]*)(\))'
#
# matches = re.search(regex, "HelloWorld('users', 'id', ColumnNotNull(), ColumnDefault('xd'))")
# next_one = matches.group(2)
# print(next_one)
# matches = re.findall(regex2, next_one)
# print(matches)
# print(len(matches))

#print(table.__repr__())
#print(CommandFormatter.format_command(table.__repr__()))


# print(len('AlterColumn("users", "id", "ColumnNotNull", "ColumnDefault", "ShowColumns_users")'))
#print(get_info('xd'))
a = None
exec("a = ShowColumns('users')")
print(a)
