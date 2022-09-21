from migration.column_plan_builder import ColumnPlanBuilder
from migration.table_plan_builder import TablePlanBuilder
from schema.column import Column
from schema.exceptions import InvalidColumnException, InvalidTableException
from schema.table import Table


class SchemaComparator:
    @staticmethod
    def compare_columns(real_column: Column, model_column: Column) -> dict:

        plan_builder = ColumnPlanBuilder(column_name=real_column.name, table_name='test')

        if real_column.name != model_column.name:
            raise InvalidColumnException(f'Column name mismatch: real {real_column.name} != model {model_column.name}')

        if real_column.column_type != model_column.column_type:
            raise InvalidColumnException(f'Column type mismatch for {real_column.name}')

        if real_column.not_null is True and model_column.not_null is False:
            plan_builder.drop_not_null()

        if real_column.not_null is False and model_column.not_null is True:
            plan_builder.add_not_null()

        if real_column.key == 'PRI' and model_column.key != 'PRI':
            raise InvalidColumnException(f'Column {real_column.name} is primary key in real schema'
                                         f' but not in model schema')

        if real_column.key == 'UNI' and model_column.key != 'UNI':
            plan_builder.drop_unique()

        if real_column.key != 'UNI' and model_column.key == 'UNI':
            plan_builder.add_unique()

        if real_column.default is not None and model_column.default is not None:
            if real_column.default != model_column.default:
                raise InvalidColumnException(f'Column {real_column.name} has different default value')
        else:
            if real_column.default is None and model_column.default is not None:
                plan_builder.add_default(model_column.default)

            if real_column.default is not None and model_column.default is None:
                plan_builder.drop_default()

        return plan_builder.get_plan()

    @staticmethod
    def compare_tables(real_table: Table, model_table: Table) -> dict:

        plan_builder = TablePlanBuilder(table_name=model_table.name, columns=model_table.columns)

        if real_table.name != model_table.name:
            raise InvalidTableException(f'Table name mismatch: real {real_table.name} != model {model_table.name}')

        for column in model_table.columns:
            if column.name not in real_table.column_names:
                plan_builder.alter_column(column.name)
            else:
                plan = SchemaComparator.compare_columns(real_table.get_column(column.name), column)
                if len(plan) > 1:
                    plan_builder.update_column(column.name, plan)

        return plan_builder.get_plan()
