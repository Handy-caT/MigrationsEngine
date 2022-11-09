from database.ddl_base.ddl_components_abstract import DDLComponent
from database.ddl_base.ddl_composites import AlterTable, AlterColumn
from database.ddl_base.ddl_leafs import ColumnNotNull, ColumnDefault, AddColumn, DropColumn, ColumnUnique, \
    DropConstraint, AddForeignKey
from database.ddl_validator import DDLValidator


def _default_plan_parser(plan):
    if plan['Action'] == 'Add':
        return ColumnDefault(plan['Value'])
    else:
        return ColumnDefault()


def _unique_plan_parser(plan):
    if plan['Action'] == 'Add':
        index = plan['Index']
        return ColumnUnique(index)
    else:
        return DropConstraint(plan['Name'])


def _foreign_key_plan_parser(plan):
    if plan['Action'] == 'Add':
        return AddForeignKey(plan['ForeignKey'])
    else:
        return DropConstraint(plan['Name'])


plan_dict = {
    'ColumnName': (lambda x: None),
    'NotNull': (lambda state: ColumnNotNull() if state == 'Add' else ColumnNotNull(False)),
    'Default': _default_plan_parser,
    'Unique': _unique_plan_parser,
    'ForeignKey': _foreign_key_plan_parser,
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

    def _parse_column(self, column_plan: dict) -> list[DDLComponent]:
        ddl_component = []
        if column_plan['Action'] == 'Update':
            column = column_plan['Column']
            alter_column = AlterColumn(column)
            sub_components = self._parse_column_plan(column_plan['Plan'])
            for sub_component in sub_components:
                if DDLValidator.can_be_child(sub_component, alter_column):
                    alter_column.add_component(sub_component)
                else:
                    ddl_component.append(sub_component)

            ddl_component.append(alter_column)
        elif column_plan['Action'] == 'Add':
            ddl_component.append(AddColumn(column_plan['Column']))
        elif column_plan['Action'] == 'Drop':
            ddl_component.append(DropColumn(column_plan['Column'].name))
        else:
            ddl_component = []

        return ddl_component

    def parse(self, plan: dict) -> DDLComponent:
        alter_table = AlterTable(plan['TableName'])

        for column_plan in plan['ColumnsPlan']:
            component = self._parse_column(column_plan)
            for sub_component in component:
                alter_table.add_component(sub_component)

        return alter_table
