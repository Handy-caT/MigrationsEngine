import pytest

from schema.column import Column
from schema.table import Table


def test_table_model_init(columns):
    name = 'Users'
    columns_arr = columns
    primary_key = ['id']

    table = Table(name, columns_arr, primary_key)

    assert table.name == name
    assert table.columns == columns
    assert table.primary_key == primary_key


def test_table_model_from_dict(columns):
    adict = {
        'Name': 'Users',
        'Columns': columns,
        'PrimaryKey': ['id']
    }

    table = Table.from_dict(adict)

    assert table.name == adict['Name']
    assert table.columns == adict['Columns']
    assert table.primary_key == adict['PrimaryKey']
