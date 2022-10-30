from database.ddl_base.ddl_composites import AlterTable, AlterColumn
from database.ddl_base.ddl_leafs import ColumnNotNull
from migration.plan_parser import PlanParser


def test_plan_parser(plan, column):
    plan_parser = PlanParser()

    alter_table = AlterTable('test')
    alter_column = AlterColumn(column)
    not_null = ColumnNotNull()

    alter_column.add_component(not_null)
    alter_table.add_component(alter_column)

    assert plan_parser.parse(plan) == alter_table
