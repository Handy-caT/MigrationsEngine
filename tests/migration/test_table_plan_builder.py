import pytest

from migration.table_plan_builder import TablePlanBuilder
from database.schema.exceptions import ColumnNotFoundException


def test_table_plan_generator_init(columns):
    table_name = 'test'
    columns_arr = columns

    table_plan_generator = TablePlanBuilder(table_name, columns_arr)

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

    table_plan_generator = TablePlanBuilder.from_dict(adict)

    assert table_plan_generator.table_name == adict['TableName']
    assert table_plan_generator.columns == adict['Columns']
    assert table_plan_generator.get_plan() == {
        'TableName': adict['TableName'],
        'ColumnsPlan': [],
        'IndexPlan': []
    }


def test_table_plan_add_column(table_plan_generator, columns):
    table_plan_generator.add_column(columns[0])

    assert table_plan_generator.get_plan() == {
        'TableName': 'test',
        'ColumnsPlan': [
            {
                'Column': columns[0],
                'Action': 'Add'
            }
            ],
        'IndexPlan': []
    }


def test_table_plan_add_column_not_found(table_plan_generator):
    with pytest.raises(ColumnNotFoundException):
        table_plan_generator.add_column('not_found')

    assert table_plan_generator.get_plan() == {
        'TableName': 'test',
        'ColumnsPlan': [],
        'IndexPlan': []
    }


def test_table_plan_drop_column(table_plan_generator, columns):
    table_plan_generator.drop_column(columns[0])

    assert table_plan_generator.get_plan() == {
        'TableName': 'test',
        'ColumnsPlan': [
            {
                'Column': columns[0],
                'Action': 'Drop'
            }
            ],
        'IndexPlan': []
    }


def test_table_plan_drop_column_not_found(table_plan_generator):
    with pytest.raises(ColumnNotFoundException):
        table_plan_generator.drop_column('not_found')

    assert table_plan_generator.get_plan() == {
        'TableName': 'test',
        'ColumnsPlan': [],
        'IndexPlan': []
    }


def test_table_plan_add_index(table_plan_generator, columns):
    table_plan_generator.add_index(columns[0])

    assert table_plan_generator.get_plan() == {
        'TableName': 'test',
        'ColumnsPlan': [],
        'IndexPlan': [
            {
                'Column': columns[0],
                'Action': 'Add'
            }
            ]
    }


def test_table_plan_add_index_not_found(table_plan_generator):
    with pytest.raises(ColumnNotFoundException):
        table_plan_generator.add_index('not_found')

    assert table_plan_generator.get_plan() == {
        'TableName': 'test',
        'ColumnsPlan': [],
        'IndexPlan': []
    }


def test_table_plan_update_column(table_plan_generator, column_plan_generator, columns):
    plan = column_plan_generator.get_plan()
    table_plan_generator.update_column(columns[0], plan)

    assert table_plan_generator.get_plan() == {
        'TableName': 'test',
        'ColumnsPlan': [
            {
                'Column': columns[0],
                'Action': 'Update',
                'Plan': plan
            }
            ],
        'IndexPlan': []
    }
