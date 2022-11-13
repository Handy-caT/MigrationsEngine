from database.dialects.mysql.mysql_interpreter import MySqlInterpreter
from migration.plan_parser import PlanParser
from migration.schema_comparator import SchemaComparator


def test_compare_two_tables_add_column(table, column):
    real_table = table
    model_table = table.__copy__()

    model_table.columns.append(column)

    plan = SchemaComparator.compare_tables(real_table, model_table)

    plan_parser = PlanParser()
    component = plan_parser.parse(plan)
    interpreter = MySqlInterpreter()
    translated_plan = interpreter.interpret(component)

    assert translated_plan == ['ALTER TABLE Users ADD COLUMN password VARCHAR(40);']


def test_compare_two_tables_update_column_add(table, column_updated):
    real_table = table
    model_table = table.__copy__()

    model_table.columns[1] = column_updated

    plan = SchemaComparator.compare_tables(real_table, model_table)

    plan_parser = PlanParser()
    component = plan_parser.parse(plan)
    interpreter = MySqlInterpreter()
    translated_plan = interpreter.interpret(component)

    assert translated_plan == ['ALTER TABLE Users ADD CONSTRAINT name_unique UNIQUE (name);',
                               'ALTER TABLE Users MODIFY COLUMN name VARCHAR(40) DEFAULT test NOT NULL;']


def test_compare_two_tables_update_column_drop(table, column_updated):
    real_table = table
    model_table = table.__copy__()

    real_table.columns[1] = column_updated

    plan = SchemaComparator.compare_tables(real_table, model_table)

    plan_parser = PlanParser()
    component = plan_parser.parse(plan)
    interpreter = MySqlInterpreter()
    translated_plan = interpreter.interpret(component)

    assert translated_plan == ['ALTER TABLE Users DROP CONSTRAINT name_unique;',
                               'ALTER TABLE Users ALTER COLUMN name DROP DEFAULT;',
                               'ALTER TABLE Users MODIFY COLUMN name VARCHAR(40) NULL;']
