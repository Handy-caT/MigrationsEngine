from sqlalchemy import Column, String, ForeignKey

column = Column('data', String(40), ForeignKey('users.id'))

print(column.__dict__)

print(column.key)

print(column.type)

print(column.name)
