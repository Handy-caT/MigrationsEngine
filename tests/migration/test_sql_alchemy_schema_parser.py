import sqlalchemy


def test_parse_column(parser):
    column = parser.parse_column(sqlalchemy.schema.Column('id', sqlalchemy.Integer))

    assert column.name == 'id'
    assert column.column_type == 'integer'
    assert column.default is None
    assert column.not_null is False
    assert column.foreign_key is None
    assert column.key is None


def test_foreign_key(parser):
    column = sqlalchemy.schema.Column('id', sqlalchemy.Integer, sqlalchemy.schema.ForeignKey('users.id'))
    column = parser.parse_column(column)

    assert column.foreign_key is not None
    assert column.foreign_key.name == 'fk_users_id'
    assert column.foreign_key.column_name == 'id'
    assert column.foreign_key.key_table == 'users'
    assert column.foreign_key.key_column == 'id'
