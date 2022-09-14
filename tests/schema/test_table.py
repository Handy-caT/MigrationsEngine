import pytest

from schema.column import Column
from schema.exceptions.column_not_found_exception import ColumnNotFoundException
from schema.exceptions.invalid_column_exception import InvalidColumnException
from schema.table import Table


def test_table_model_init(columns):
    name = 'Users'
    columns_arr = columns
    primary_key = ['id']

    table = Table(name, columns_arr)

    assert table.name == name
    assert table.columns == columns
    assert table.get_primary_key() == primary_key


def test_table_model_from_dict(columns):
    adict = {
        'Name': 'Users',
        'Columns': columns,
        'PrimaryKey': ['id']
    }

    table = Table.from_dict(adict)

    assert table.name == adict['Name']
    assert table.columns == adict['Columns']
    assert table.get_primary_key() == adict['PrimaryKey']


def test_table_model_init_with_wrong_column(columns):
    name = 'Users'
    columns_arr = columns
    columns_arr[0].not_null = False

    with pytest.raises(InvalidColumnException):
        Table(name, columns_arr)


def test_table_model_set_primary_key(columns):
    name = 'Users'
    columns_arr = columns
    primary_key = ['id', 'name']

    table = Table(name, columns_arr)
    table.set_primary_key(primary_key)

    assert table.get_primary_key() == primary_key
    assert table.columns[1].key == 'PRI'
    assert table.columns[1].not_null is True


def test_table_model_init_not_unique_columns(columns):
    name = 'Users'
    columns_arr = columns
    columns_arr.append(columns_arr[0])

    table = Table(name, columns_arr)

    assert len(table.columns) == len(columns_arr) - 1


def test_table_model_add_column(columns):
    name = 'Users'
    columns_arr = columns
    column = Column(
        name='password',
        column_type='varchar(40)',
        not_null=False,
        key=None,
        default=None,
        extra=None
    )

    table = Table(name, columns_arr)
    table.add_column(column)

    assert len(table.columns) == len(columns_arr) + 1
    assert table.columns[-1] == column


def test_table_model_add_not_unique_column(columns):
    name = 'Users'
    columns_arr = columns
    column = columns[1]

    table = Table(name, columns_arr)
    table.add_column(column)

    assert len(table.columns) == len(columns_arr)


def test_table_model_remove_column(columns):
    name = 'Users'
    columns_arr = columns
    column_name = 'name'

    table = Table(name, columns_arr)
    table.remove_column(column_name)

    assert len(table.columns) == len(columns_arr) - 1


def test_table_model_not_remove_primary_key(columns):
    name = 'Users'
    columns_arr = columns
    column_name = 'id'

    table = Table(name, columns_arr)

    with pytest.raises(InvalidColumnException):
        table.remove_column(column_name)


def test_table_model_remove_not_found(columns):
    name = 'Users'
    columns_arr = columns
    column_name = 'password'

    table = Table(name, columns_arr)

    with pytest.raises(ColumnNotFoundException):
        table.remove_column(column_name)
