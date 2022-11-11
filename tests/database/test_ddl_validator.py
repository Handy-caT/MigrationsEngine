import pytest

from database.ddl_base.ddl_composites import AlterColumn
from database.ddl_base.ddl_leafs import ColumnNotNull, ColumnDefault, ShowColumns
from database.ddl_validator import DDLValidator, ValidationException


def test_ddl_validator_alter_column_child_list(column):
    child_list = [
        ColumnNotNull(),
        ColumnDefault('xd'),
    ]

    for child in child_list:
        assert DDLValidator.can_be_child(child, AlterColumn(column))


def test_validate_component_valid(composite_ddl):
    assert DDLValidator.validate_component(composite_ddl) is True


def test_validate_component_invalid(composite_ddl, column):
    composite_ddl.add_component(AlterColumn(column))
    composite_ddl.components[0].add_component(ShowColumns('test'))
    with pytest.raises(ValidationException):
        DDLValidator.validate_component(composite_ddl)
