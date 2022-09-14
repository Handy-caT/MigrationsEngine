import pytest

from schema.database import Database
from schema.exceptions.invalid_table_exception import InvalidTableException
from schema.table import Table


def test_database_model_init(tables):
    name = 'test'
    tables_arr = tables

    database = Database(name, tables_arr)

    assert database.name == name
    assert database.tables == tables


def test_database_model_from_dict(tables):
    adict = {
        'Name': 'test',
        'Tables': tables
    }

    database = Database.from_dict(adict)

    assert database.name == adict['Name']
    assert database.tables == adict['Tables']


def test_database_model_add_table(tables):
    database = Database('test', tables)
    table = Table('test2', [])

    database.add_table(table)

    assert len(database.tables) == len(tables) + 1
    assert database.tables[-1] == table


def test_database_model_add_not_unique_table(tables):
    database = Database('test', tables)
    table = tables[0]

    database.add_table(table)

    assert len(database.tables) == len(tables)


def test_database_model_init_not_unique_tables(tables):
    tables.append(tables[0])

    database = Database('test', tables)

    assert database.name == 'test'
    assert len(database.tables) == len(tables) - 1


def test_database_model_remove_table(tables):
    database = Database('test', tables)
    table_name = tables[0].name

    database.remove_table(table_name)

    assert len(database.tables) == len(tables) - 1
    assert database.tables[0].name != table_name


def test_database_model_remove_not_existing_table(tables):
    database = Database('test', tables)
    table_name = 'test2'

    with pytest.raises(InvalidTableException):
        database.remove_table(table_name)
