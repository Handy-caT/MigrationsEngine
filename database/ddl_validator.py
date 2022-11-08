from database.ddl_base.ddl_components_abstract import DDLComponent
from database.ddl_base.ddl_composites import AlterTable, AlterColumn
from database.ddl_base.ddl_leafs import AddColumn, ColumnNotNull, ColumnDefault, DropColumn, ColumnUnique, AddForeignKey

_alter_column_child_list = [
    ColumnNotNull,
    ColumnDefault,
]

child_dict = {
    AlterColumn.__name__: _alter_column_child_list,
}


class DDLValidator:
    @staticmethod
    def can_be_child(child: DDLComponent, parent: DDLComponent):
        return child.__class__ in child_dict[parent.__class__.__name__]
