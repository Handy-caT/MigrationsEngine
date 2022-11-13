import pytest

from migration.schema_comparator import SchemaComparator
from database.schema.exceptions import InvalidColumnException, InvalidTableException


def test_schema_comparator_columns_not_null(column):
    real_column = column

    model_column = column.__copy__()
    model_column.not_null = True

    plan = SchemaComparator.compare_columns(real_column, model_column)

    assert plan is not None
    assert plan == {
        'Column': column,
        'NotNull': 'Add'
    }


def test_schema_comparator_columns_invalid_not_null(column):
    real_column = column
    real_column.not_null = True

    model_column = column.__copy__()
    model_column.not_null = False

    plan = SchemaComparator.compare_columns(real_column, model_column)

    assert plan is not None
    assert plan == {
        'Column': column,
        'NotNull': 'Drop'
    }


def test_schema_comparator_columns_with_different_name(column):
    real_column = column

    model_column = column.__copy__()
    model_column.name = 'different_name'

    with pytest.raises(InvalidColumnException):
        SchemaComparator.compare_columns(real_column, model_column)


def test_schema_comparator_columns_with_different_type(column):
    real_column = column

    model_column = column.__copy__()
    model_column.column_type = 'different_type'

    with pytest.raises(InvalidColumnException):
        SchemaComparator.compare_columns(real_column, model_column)


def test_schema_comparator_columns_with_different_default(column):
    real_column = column
    real_column.default = 'default'

    model_column = column.__copy__()
    model_column.default = 'different_default'

    with pytest.raises(InvalidColumnException):
        SchemaComparator.compare_columns(real_column, model_column)


def test_schema_comparator_columns_with_different_default_add(column):
    real_column = column
    real_column.default = None

    model_column = column.__copy__()
    model_column.default = 'different_default'

    plan = SchemaComparator.compare_columns(real_column, model_column)

    assert plan is not None
    assert plan == {
        'Column': column,
        'Default': {
            'Action': 'Add',
            'Value': 'different_default'
        }
    }


def test_schema_comparator_columns_with_different_default_drop(column):
    real_column = column
    real_column.default = 'different_default'

    model_column = column.__copy__()
    model_column.default = None

    plan = SchemaComparator.compare_columns(real_column, model_column)

    assert plan is not None
    assert plan == {
        'Column': column,
        'Default': {
            'Action': 'Drop'
        }
    }


def test_schema_comparator_tables_with_different_name(tables):
    real_table = tables[0]
    model_table = tables[1]

    with pytest.raises(InvalidTableException):
        SchemaComparator.compare_tables(real_table, model_table)


def test_schema_comparator_tables_with_different_columns_add(table, column):
    real_table = table
    model_table = table.__copy__()

    model_table.columns.append(column)

    plan = SchemaComparator.compare_tables(real_table, model_table)

    assert plan is not None
    assert plan == {
        'TableName': table.name,
        'ColumnsPlan': [
            {
                'Column': column,
                'Action': 'Add'
            }
        ],
        'IndexPlan': []
    }


def test_schema_comparator_tables_with_different_columns_update(table, column):
    real_table = table
    model_table = table.__copy__()

    real_column = column
    real_column.default = None

    model_column = column.__copy__()
    model_column.default = 'different_default'

    model_table.columns.append(model_column)
    real_table.columns.append(real_column)

    plan = SchemaComparator.compare_tables(real_table, model_table)

    assert plan is not None
    assert plan == {
        'TableName': table.name,
        'ColumnsPlan': [
            {
                'Column': model_column,
                'Action': 'Update',
                'Plan': {
                    'Column': real_column,
                    'Default': {
                        'Action': 'Add',
                        'Value': 'different_default'
                    }
                }
            }
        ],
        'IndexPlan': []
    }
