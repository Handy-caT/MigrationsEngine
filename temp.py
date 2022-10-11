from sqlalchemy import Column, String, ForeignKey

import schema.column
from database.ddl_components_abstract import DDLComponent, DDLComposite
from database.ddl_composites import AlterTable, AddColumn

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

