from migration.column_plan_builder import ColumnPlanBuilder
from schema.exceptions import InvalidColumnException


class SchemaComparator:
    @staticmethod
    def compare_columns(real_column, model_column):

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

        return plan_builder.get_plan()s
