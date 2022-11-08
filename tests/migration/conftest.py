import pytest

from database.schema.index import Index


@pytest.fixture(scope='function')
def unique(column):
    return Index(f'{column.name}_unique', [column.name], True)


@pytest.fixture(scope='function')
def plan_update(column, unique):
    return {'TableName': 'test',
            'ColumnsPlan': [
                {
                    'Column': column,
                    'Action': 'Update',
                    'Plan': {
                        'ColumnName': column.name,
                        'NotNull': 'Add',
                        'Default': {
                            'Action': 'Add',
                            'Value': 'xd'
                        },
                        'Unique': {
                            'Action': 'Add',
                            'Index': unique
                        }
                    }
                }
            ],
            'IndexPlan': []
            }


@pytest.fixture(scope='function')
def plan_drop(column):
    return {'TableName': 'test',
            'ColumnsPlan': [
                {
                    'Column': column,
                    'Action': 'Drop'
                }
            ],
            'IndexPlan': []
            }


@pytest.fixture(scope='function')
def plan_add(column):
    return {'TableName': 'test',
            'ColumnsPlan': [
                {
                    'Column': column,
                    'Action': 'Add'
                }
            ],
            'IndexPlan': []
            }
