from schema.column import Column


def test_column_model_init():
    name = 'Users'
    column_type = 'Varchar(40)'
    null = False
    key = None
    default = None
    extra = None

    column = Column(name, column_type, null, key, default, extra)

    assert column.name == name
    assert column.column_type == column_type.lower()
    assert column.null == null
    assert column.key == key
    assert column.default == default
    assert column.extra == extra


def test_column_model_from_dict():
    adict = {
        'Name': 'Users',
        'Type': 'Varchar(40)',
        'Null': False,
        'Key': None,
        'Default': None,
        'Extra': None
    }

    column = Column.from_dict(adict)

    assert column.name == adict['Name']
    assert column.column_type == adict['Type'].lower()
    assert column.null == adict['Null']
    assert column.key == adict['Key']
    assert column.default == adict['Default']
    assert column.extra == adict['Extra']
