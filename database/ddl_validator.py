from database.ddl_base.ddl_components_abstract import DDLComponent
from database.ddl_base.ddl_composites import AlterTable, AlterColumn, Composite
from database.ddl_base.ddl_leafs import AddColumn, ColumnNotNull, ColumnDefault, DropColumn, ColumnUnique, \
    AddForeignKey, DropConstraint, ShowColumns, Leaf, ColumnType, RenameColumn, RenameTable, DropTable, DropDefault

_alter_column_child_list = [
    ColumnNotNull,
    ColumnDefault,
    ColumnType,
    DropDefault,
    Leaf,
]
_alter_table_child_list = [
    AddColumn,
    DropColumn,
    AlterColumn,
    ColumnUnique,
    AddForeignKey,
    DropConstraint,
    RenameColumn,
    RenameTable,
    Leaf,
]
_composite_list = [
    AlterTable,
    ShowColumns,
    DropTable,
]

child_dict = {
    AlterColumn.__name__: _alter_column_child_list,
    AlterTable.__name__: _alter_table_child_list,
    Composite.__name__: _composite_list,
}


class ValidationException(Exception):
    def __init__(self, child: DDLComponent, parent: DDLComponent, component: DDLComponent):
        self.child = child
        self.parent = parent
        self.component = component

    def __str__(self):
        return f"Component {self.child.__class__} can't be child of {self.parent.__class__} in" + \
                   f" {self.component}"


class DDLValidator:
    @staticmethod
    def can_be_child(child: DDLComponent, parent: DDLComponent) -> bool:
        return child.__class__ in child_dict[parent.__class__.__name__]

    @staticmethod
    def validate_component(component: DDLComponent) -> bool:
        ind = False
        stack = []

        iterator = component.__iter__()
        stack.append(next(iterator))

        for i in iterator:
            if ind:
                while i not in stack[-1]:
                    stack.pop()
                ind = False

            if not DDLValidator.can_be_child(i, stack[-1]):
                raise ValidationException(i, stack[-1], component)

            if i.is_composite:
                stack.append(i)
            else:
                ind = True

        return True
