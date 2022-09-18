from migration.column_plan_builder import ColumnPlanBuilder


def test_column_plan_generator_init():
    column_name = 'id'
    table_name = 'test'

    column_plan_generator = ColumnPlanBuilder(column_name, table_name)

    assert column_plan_generator.column_name == column_name
    assert column_plan_generator.table_name == table_name
    assert column_plan_generator.get_plan() == {
        'ColumnName': column_name
    }


def test_column_plan_generator_from_dict():
    adict = {
        'ColumnName': 'id',
        'TableName': 'test'
    }

    column_plan_generator = ColumnPlanBuilder.from_dict(adict)

    assert column_plan_generator.column_name == adict['ColumnName']
    assert column_plan_generator.table_name == adict['TableName']
    assert column_plan_generator.get_plan() == {
        'ColumnName': adict['ColumnName']
    }


def test_column_plan_add_unique(column_plan_generator):
    column_plan_generator.add_unique()

    assert column_plan_generator.get_plan() == {
        'ColumnName': 'id',
        'Unique': 'Add'
    }


def test_column_plan_drop_unique(column_plan_generator):
    column_plan_generator.drop_unique()

    assert column_plan_generator.get_plan() == {
        'ColumnName': 'id',
        'Unique': 'Drop'
    }


def test_column_plan_add_not_null(column_plan_generator):
    column_plan_generator.add_not_null()

    assert column_plan_generator.get_plan() == {
        'ColumnName': 'id',
        'NotNull': 'Add'
    }


def test_column_plan_add_default(column_plan_generator):
    column_plan_generator.add_default('default')

    assert column_plan_generator.get_plan() == {
        'ColumnName': 'id',
        'Default': {
            'Action': 'Add',
            'Value': 'default'
        }
    }


def test_column_plan_add_foreign_key(column_plan_generator):
    column_plan_generator.add_foreign_key('test', 'id')

    assert column_plan_generator.get_plan() == {
        'ColumnName': 'id',
        'ForeignKey': {
            'Action': 'Add',
            'Table': 'test',
            'Column': 'id'
        }
    }


def test_column_plan_drop_foreign_key(column_plan_generator):
    column_plan_generator.drop_foreign_key()

    assert column_plan_generator.get_plan() == {
        'ColumnName': 'id',
        'ForeignKey': {
            'Action': 'Drop'
        }
    }


def test_column_plan_drop_not_null(column_plan_generator):
    column_plan_generator.drop_not_null()

    assert column_plan_generator.get_plan() == {
        'ColumnName': 'id',
        'NotNull': 'Drop'
    }


def test_column_plan_drop_default(column_plan_generator):
    column_plan_generator.drop_default()

    assert column_plan_generator.get_plan() == {
        'ColumnName': 'id',
        'Default': {
            'Action': 'Drop'
        }
    }
