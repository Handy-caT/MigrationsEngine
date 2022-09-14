import pytest

from schema.column import Column
from schema.table import Table


@pytest.fixture(scope='package')
def columns():
    column1 = Column(
        name='id',
        column_type='int',
        null=False,
        key='PRI',
        default=None,
        extra='auto_increment'
    )

    column2 = Column(
        name='name',
        column_type='varchar(40)',
        null=False,
        key=None,
        default=None,
        extra=None
    )

    column3 = Column(
        name='email',
        column_type='varchar(40)',
        null=False,
        key=None,
        default=None,
        extra=None
    )

    return [column1, column2, column3]


@pytest.fixture(scope='module')
def tables(columns):
    table1 = Table(
        name='Users',
        columns=columns,
        primary_key=['id']
    )

    table2 = Table(
        name='Posts',
        columns=columns,
        primary_key=['id']
    )

    return [table1, table2]
