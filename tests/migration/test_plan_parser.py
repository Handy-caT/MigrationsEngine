from database.ddl_base.ddl_composites import AlterTable, AlterColumn
from database.ddl_base.ddl_leafs import ColumnNotNull, ColumnDefault, AddColumn, DropColumn, ColumnUnique
from migration.plan_parser import PlanParser


def test_plan_parser_update(plan_update, column, unique):
    plan_parser = PlanParser()

    alter_table = AlterTable('test')
    alter_column = AlterColumn(column)
    not_null = ColumnNotNull()
    default = ColumnDefault('xd')

    alter_column.add_component(not_null)
    alter_column.add_component(default)
    alter_table.add_component(ColumnUnique(unique))
    alter_table.add_component(alter_column)

    assert plan_parser.parse(plan_update) == alter_table


def test_plan_parser_add(plan_add, column):
    plan_parser = PlanParser()

    alter_table = AlterTable('test')
    add_column = AddColumn(column)

    alter_table.add_component(add_column)

    assert plan_parser.parse(plan_add) == alter_table


def test_plan_parser_drop(plan_drop, column):
    plan_parser = PlanParser()

    alter_table = AlterTable('test')
    drop_column = DropColumn(column.name)

    alter_table.add_component(drop_column)

    assert plan_parser.parse(plan_drop) == alter_table
