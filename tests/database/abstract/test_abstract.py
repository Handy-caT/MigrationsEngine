import pytest

from database.ddl_base.ddl_components_abstract import DDLComponent, DDLComposite, DDLLeaf


def test_abstract_component():
    with pytest.raises(TypeError):
        DDLComponent()


def test_abstract_composite():
    with pytest.raises(TypeError):
        DDLComposite()


def test_abstract_leaf():
    with pytest.raises(TypeError):
        DDLLeaf()
