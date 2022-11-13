import pytest

from database.schema.index import Index


@pytest.fixture(scope='function')
def unique(column):
    return Index(f'{column.name}_unique', [column.name], True)


@pytest.fixture(scope='function')
def plan_update_add(column, unique, foreign_key):
    return {'TableName': 'test',
            'ColumnsPlan': [
                {
                    'Column': column,
                    'Action': 'Update',
                    'Plan': {
                        'Column': column,
                        'NotNull': 'Add',
                        'Default': {
                            'Action': 'Add',
                            'Value': 'xd'
                        },
                        'Unique': {
                            'Action': 'Add',
                            'Index': unique
                        },
                        'ForeignKey': {
                            'Action': 'Add',
                            'ForeignKey': foreign_key
                        }
                    }
                }
            ],
            'IndexPlan': []
            }


@pytest.fixture(scope='function')
def plan_update_drop(column, unique):
    return {'TableName': 'test',
            'ColumnsPlan': [
                {
                    'Column': column,
                    'Action': 'Update',
                    'Plan': {
                        'Column': column,
                        'NotNull': 'Drop',
                        'Default': {
                            'Action': 'Drop',
                        },
                        'Unique': {
                            'Action': 'Drop',
                            'Name': unique.name
                        },
                        'ForeignKey': {
                            'Action': 'Drop',
                            'Name': f'{column.name}_foreign_key'
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
