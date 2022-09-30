from sqlalchemy import Column, String, ForeignKey

column = Column('data', String(40), ForeignKey('users.id'), autoincrement=True)

for i in column.foreign_keys:
    print(i.target_fullname)

print(column.key)

print(column.type)

print(column.default)
