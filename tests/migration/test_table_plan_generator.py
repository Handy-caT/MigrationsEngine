import pytest

from migration.table_plan_generator import TablePlanGenerator
from schema.exceptions import ColumnNotFoundException


def test_table_plan_generator_init(columns):
    table_name = 'test'
    columns_arr = columns

    table_plan_generator = TablePlanGenerator(table_name, columns_arr)

    assert table_plan_generator.table_name == table_name
    assert table_plan_generator.columns == columns_arr
    assert table_plan_generator.get_plan() == {
        'TableName': table_name,
        'ColumnsPlan': [],
        'IndexPlan': []
    }


def test_table_plan_from_dict(columns):
    adict = {
        'TableName': 'test',
        'Columns': columns
    }

    table_plan_generator = TablePlanGenerator.from_dict(adict)

    assert table_plan_generator.table_name == adict['TableName']
    assert table_plan_generator.columns == adict['Columns']
    assert table_plan_generator.get_plan() == {
        'TableName': adict['TableName'],
        'ColumnsPlan': [],
        'IndexPlan': []
    }


def test_table_plan_add_column(table_plan_generator):
    table_plan_generator.alter_column('id')

    assert table_plan_generator.get_plan() == {
        'TableName': 'test',
        'ColumnsPlan': [
            {
                'Column': 'id',
                'Action': 'Alter'
            }
            ],
        'IndexPlan': []
    }


def test_table_plan_add_column_not_found(table_plan_generator):
    with pytest.raises(ColumnNotFoundException):
        table_plan_generator.alter_column('not_found')

    assert table_plan_generator.get_plan() == {
        'TableName': 'test',
        'ColumnsPlan': [],
        'IndexPlan': []
    }


def test_table_plan_drop_column(table_plan_generator):
    table_plan_generator.drop_column('id')

    assert table_plan_generator.get_plan() == {
        'TableName': 'test',
        'ColumnsPlan': [
            {
                'Column': 'id',
                'Action': 'Drop'
            }
            ],
        'IndexPlan': []
    }
