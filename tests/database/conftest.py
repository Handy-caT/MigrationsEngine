import pytest

from database.ddl_base.ddl_composites import Composite, AlterTable, AlterColumn
from database.ddl_base.ddl_leafs import ColumnNotNull, ColumnDefault, ShowColumns
from database.dialects.default.translate_dict import translate_dict_default
from database.translator import Translator


@pytest.fixture(scope='function')
def composite_ddl(column):
    composite = Composite()

    alter_table = AlterTable('users')

    alter_column = AlterColumn(column)
    alter_column.add_component(ColumnNotNull())
    alter_column.add_component(ColumnDefault('xd'))

    alter_table.add_component(alter_column)
    composite.add_component(alter_table)
    composite.add_component(ShowColumns('users'))

    return composite


@pytest.fixture(scope='function')
def default_translator():
    return Translator(translate_dict_default)
