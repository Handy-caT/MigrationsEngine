import pytest

from migration.schema_comparator import SchemaComparator
from schema.exceptions import InvalidColumnException


def test_schema_comparator_columns_not_null(column):
    real_column = column

    model_column = column.__copy__()
    model_column.not_null = True

    plan = SchemaComparator.compare_columns(real_column, model_column)

    assert plan is not None
    assert plan == {
        'ColumnName': column.name,
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
        'ColumnName': column.name,
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
        'ColumnName': column.name,
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
        'ColumnName': column.name,
        'Default': {
            'Action': 'Drop'
        }
    }
