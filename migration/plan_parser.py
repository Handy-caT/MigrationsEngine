from database.ddl_base.ddl_components_abstract import DDLComponent
from database.ddl_base.ddl_composites import AlterTable, AlterColumn
from database.ddl_base.ddl_leafs import ColumnNotNull, ColumnDefault, AddColumn, DropColumn, DropDefault, ColumnUnique
from database.schema.index import Index


def _default_plan_parser(plan):
    if plan['Action'] == 'Add':
        return ColumnDefault(plan['Value'])
    else:
        return DropDefault()


def _unique_plan_parser(plan):
    if plan['Action'] == 'Add':
        index = plan['Index']
        return ColumnUnique(index)
    else:
        return


plan_dict = {
    'ColumnName': (lambda x: None),
    'NotNull': (lambda state: ColumnNotNull() if state == 'Add' else ColumnNotNull(False)),
    'Default': _default_plan_parser,
    'Unique': (lambda x: ColumnUnique() if x == 'Add' else DropUnique()),
}


class PlanParser:

    @staticmethod
    def _parse_column_plan(column_plan: dict) -> list[DDLComponent]:
        sub_components = []
        for key, value in column_plan.items():
            component = plan_dict[key](value)
            if component is not None:
                sub_components.append(component)

        return sub_components

    def _parse_column(self, column_plan: dict) -> DDLComponent:
        ddl_component = None
        if column_plan['Action'] == 'Update':
            column = column_plan['Column']
            alter_column = AlterColumn(column)
            sub_components = self._parse_column_plan(column_plan['Plan'])
            for sub_component in sub_components:
                alter_column.add_component(sub_component)

            ddl_component = alter_column
        elif column_plan['Action'] == 'Add':
            ddl_component = AddColumn(column_plan['Column'])
        elif column_plan['Action'] == 'Drop':
            ddl_component = DropColumn(column_plan['Column'].name)
        else:
            ddl_component = None

        return ddl_component

    def parse(self, plan: dict) -> DDLComponent:
        alter_table = AlterTable(plan['TableName'])

        for column_plan in plan['ColumnsPlan']:
            component = self._parse_column(column_plan)
            if component is not None:
                alter_table.add_component(component)

        return alter_table
