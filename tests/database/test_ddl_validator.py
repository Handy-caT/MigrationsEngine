from database.ddl_base.ddl_composites import AlterColumn
from database.ddl_base.ddl_leafs import ColumnNotNull, ColumnDefault
from database.ddl_validator import DDLValidator


def test_ddl_validator_alter_column_child_list(column):
    child_list = [
        ColumnNotNull(),
        ColumnDefault('xd'),
    ]

    for child in child_list:
        assert DDLValidator.can_be_child(child, AlterColumn(column))
