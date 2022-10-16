import pytest

from database.translators.default_translator import DefaultTranslator
from migration.column_plan_builder import ColumnPlanBuilder
from migration.sql_alchemy_schema_parser import SQLAlchemySchemaParser
from migration.table_plan_builder import TablePlanBuilder
from schema.column import Column
from schema.foreign_key import ForeignKey
from schema.table import Table
from database.ddl_base.ddl_composites import Composite, AlterTable, AlterColumn
from database.ddl_base.ddl_leafs import ColumnNotNull, ColumnDefault, ShowColumns


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
        name='password',
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
def table(columns):
    return Table(
        name='Users',
        columns=columns,
    )


@pytest.fixture(scope='function')
def table_plan_generator(columns):
    return TablePlanBuilder('test', columns)


@pytest.fixture(scope='function')
def column_plan_generator():
    return ColumnPlanBuilder(column_name='id', table_name='test')


@pytest.fixture(scope='function')
def foreign_key():
    return ForeignKey(
        name='fk_test',
        column_name='test_id',
        key_table='test',
        key_column='id'
    )


@pytest.fixture(scope='function')
def parser():
    return SQLAlchemySchemaParser()


@pytest.fixture(scope='function')
def composite_ddl():
    composite = Composite()

    alter_table = AlterTable('users')

    alter_column = AlterColumn('data')
    alter_column.add_component(ColumnNotNull())
    alter_column.add_component(ColumnDefault('xd'))

    alter_table.add_component(alter_column)
    composite.add_component(alter_table)
    composite.add_component(ShowColumns('users'))

    return composite


@pytest.fixture(scope='function')
def default_translator():
    return DefaultTranslator()
