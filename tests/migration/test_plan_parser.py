from database.ddl_base.ddl_composites import AlterTable, AlterColumn
from database.ddl_base.ddl_leafs import ColumnNotNull, ColumnDefault, AddColumn, DropColumn, ColumnUnique, \
    DropConstraint, AddForeignKey, DropDefault
from migration.plan_parser import PlanParser


def test_plan_parser_update_add(plan_update_add, column, unique, foreign_key):
    plan_parser = PlanParser()

    alter_table = AlterTable('test')
    alter_column = AlterColumn(column)
    not_null = ColumnNotNull()
    default = ColumnDefault('xd')

    alter_column.add_component(not_null)
    alter_column.add_component(default)
    alter_table.add_component(ColumnUnique(unique))
    alter_table.add_component(AddForeignKey(foreign_key))
    alter_table.add_component(alter_column)

    assert plan_parser.parse(plan_update_add) == alter_table


def test_plan_parser_update_drop(plan_update_drop, column, unique, foreign_key):
    plan_parser = PlanParser()

    alter_table = AlterTable('test')
    alter_column = AlterColumn(column)
    not_null = ColumnNotNull(not_null=False)
    default = DropDefault()

    alter_column.add_component(not_null)
    alter_column.add_component(default)
    alter_table.add_component(DropConstraint(unique.name))
    alter_table.add_component(DropConstraint(foreign_key.name))
    alter_table.add_component(alter_column)

    assert plan_parser.parse(plan_update_drop) == alter_table


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
