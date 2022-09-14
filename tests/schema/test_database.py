import pytest

from schema.database import Database
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