import pytest

from migration.column_plan_builder import ColumnPlanBuilder
from migration.table_plan_builder import TablePlanBuilder
from schema.column import Column
from schema.table import Table


@pytest.fixture(scope='function')
def columns():
    return [
        Column(
            name='id',
            column_type='int',
            not_null=True,
            key='PRI',
            default=None,
            extra='auto_increment'
        ),
        Column(
            name='name',
            column_type='varchar(40)',
            not_null=False,
            key=None,
            default=None,
            extra=None
        ),
        Column(
            name='email',
            column_type='varchar(40)',
            not_null=False,
            key=None,
            default=None,
            extra=None
        )
    ]


@pytest.fixture(scope='function')
def column():
    return Column(
        name='name',
        column_type='varchar(40)',
        not_null=False,
        key=None,
        default=None,
        extra=None
    )


@pytest.fixture(scope='function')
def tables(columns):
    table1 = Table(
        name='Users',
        columns=columns,
    )

    table2 = Table(
        name='Posts',
        columns=columns,
    )

    return [table1, table2]


@pytest.fixture(scope='function')
def table_plan_generator(columns):
    return TablePlanBuilder('test', columns)


@pytest.fixture(scope='function')
def column_plan_generator():
    return ColumnPlanBuilder(column_name='id', table_name='test')
