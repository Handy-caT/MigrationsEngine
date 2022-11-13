from database.schema.index import Index
from migration.column_plan_builder import ColumnPlanBuilder


def test_column_plan_generator_init(column):
    table_name = 'test'

    column_plan_generator = ColumnPlanBuilder(column, table_name)

    assert column_plan_generator.column == column
    assert column_plan_generator.table_name == table_name
    assert column_plan_generator.get_plan() == {
        'Column': column
    }


def test_column_plan_generator_from_dict(column):
    adict = {
        'Column': column,
        'TableName': 'test'
    }

    column_plan_generator = ColumnPlanBuilder.from_dict(adict)

    assert column_plan_generator.column == adict['Column']
    assert column_plan_generator.table_name == adict['TableName']
    assert column_plan_generator.get_plan() == {
        'Column': adict['Column']
    }


def test_column_plan_add_unique(column_plan_generator, column):
    column_plan_generator.add_unique()
    index = Index(f'{column.name}_unique', [column.name], True)

    assert column_plan_generator.get_plan() == {
        'Column': column,
        'Unique': {
            'Action': 'Add',
            'Index': index
        }
    }


def test_column_plan_add_unique_with_name(column_plan_generator, column):
    column_plan_generator.add_unique('unique_name')
    index = Index('unique_name', [column.name], True)

    assert column_plan_generator.get_plan() == {
        'Column': column,
        'Unique': {
            'Action': 'Add',
            'Index': index
        }
    }


def test_column_plan_drop_unique_with_name(column_plan_generator, column):
    column_plan_generator.drop_unique('unique_name')

    assert column_plan_generator.get_plan() == {
        'Column': column,
        'Unique': {
            'Action': 'Drop',
            'Name': 'unique_name'
        }
    }


def test_column_plan_drop_unique(column_plan_generator, column):
    column_plan_generator.drop_unique()

    assert column_plan_generator.get_plan() == {
        'Column': column,
        'Unique': {
            'Action': 'Drop',
            'Name': f'{column.name}_unique'
        }
    }


def test_column_plan_add_not_null(column_plan_generator, column):
    column_plan_generator.add_not_null()

    assert column_plan_generator.get_plan() == {
        'Column': column,
        'NotNull': 'Add'
    }


def test_column_plan_add_default(column_plan_generator, column):
    column_plan_generator.add_default('default')

    assert column_plan_generator.get_plan() == {
        'Column': column,
        'Default': {
            'Action': 'Add',
            'Value': 'default'
        }
    }


def test_column_plan_add_foreign_key(column_plan_generator, foreign_key, column):
    column_plan_generator.add_foreign_key(foreign_key)

    assert column_plan_generator.get_plan() == {
        'Column': column,
        'ForeignKey': {
            'Action': 'Add',
            'ForeignKey': foreign_key
        }
    }


def test_column_plan_drop_foreign_key(column_plan_generator, column):
    column_plan_generator.drop_foreign_key()

    assert column_plan_generator.get_plan() == {
        'Column': column,
        'ForeignKey': {
            'Action': 'Drop',
            'Name': f'{column.name}_foreign_key'
        }
    }


def test_column_plan_drop_foreign_key_with_name(column_plan_generator, column):
    column_plan_generator.drop_foreign_key('foreign_key_name')

    assert column_plan_generator.get_plan() == {
        'Column': column,
        'ForeignKey': {
            'Action': 'Drop',
            'Name': 'foreign_key_name'
        }
    }


def test_column_plan_drop_not_null(column_plan_generator, column):
    column_plan_generator.drop_not_null()

    assert column_plan_generator.get_plan() == {
        'Column': column,
        'NotNull': 'Drop'
    }


def test_column_plan_drop_default(column_plan_generator, column):
    column_plan_generator.drop_default()

    assert column_plan_generator.get_plan() == {
        'Column': column,
        'Default': {
            'Action': 'Drop'
        }
    }
