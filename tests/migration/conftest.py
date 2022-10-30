import pytest


@pytest.fixture(scope='function')
def plan(column):
    return {'TableName': 'test',
            'ColumnsPlan': [
                {
                    'Column': column,
                    'Action': 'Update',
                    'Plan': {
                        'ColumnName': column.name,
                        'NotNull': 'Add'
                    }
                }
            ],
            'IndexPlan': []
            }
