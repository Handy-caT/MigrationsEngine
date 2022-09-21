from schema.foreign_key import ForeignKey


def test_foreign_key_init():
    name = 'fk_users_id'
    column_name = 'user_id'
    key_column = 'id'
    key_table = 'users'

    foreign_key = ForeignKey(name, column_name, key_table, key_column)

    assert foreign_key.name == name
    assert foreign_key.column_name == column_name
    assert foreign_key.key_column == key_column
    assert foreign_key.key_table == key_table


def test_foreign_key_from_dict():
    name = 'fk_users_id'
    column_name = 'user_id'
    key_column = 'id'
    key_table = 'users'

    foreign_key = ForeignKey.from_dict({
        'Name': name,
        'Column': column_name,
        'KeyTable': key_table,
        'KeyColumn': key_column
    })

    assert foreign_key.name == name
    assert foreign_key.column_name == column_name
    assert foreign_key.key_column == key_column
    assert foreign_key.key_table == key_table
