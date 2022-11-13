from database.schema.column import Column


def test_column_model_init():
    name = 'Users'
    column_type = 'Varchar(40)'
    not_null = False
    key = None
    default = None
    extra = None
    foreign_key = None

    column = Column(name, column_type, not_null, key, default, extra, foreign_key)

    assert column.name == name
    assert column.column_type == column_type.upper()
    assert column.not_null == not_null
    assert column.key == key
    assert column.default == default
    assert column.extra == extra
    assert column.foreign_key == foreign_key


def test_column_model_from_dict():
    adict = {
        'Name': 'Users',
        'Type': 'Varchar(40)',
        'NotNull': False,
        'Key': None,
        'Default': None,
        'Extra': None,
        'ForeignKey': None,
    }

    column = Column.from_dict(adict)

    assert column.name == adict['Name']
    assert column.column_type == adict['Type'].upper()
    assert column.not_null == adict['NotNull']
    assert column.key == adict['Key']
    assert column.default == adict['Default']
    assert column.extra == adict['Extra']
    assert column.foreign_key == adict['ForeignKey']
