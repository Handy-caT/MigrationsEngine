from schema.index import Index


def test_index_init():
    name = 'idx_users_id'
    columns = ['user_id']
    unique = False

    index = Index(name, columns, unique)

    assert index.name == name
    assert index.columns == columns
    assert index.unique == unique


def test_index_from_dict():
    name = 'idx_users_id'
    columns = ['user_id']
    unique = False

    index = Index.from_dict({
        'Name': name,
        'Columns': columns,
        'Unique': unique
    })

    assert index.name == name
    assert index.columns == columns
    assert index.unique == unique
