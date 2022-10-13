from database.abstract_translator import AbstractTranslator
from database.ddl_base.ddl_components_abstract import DDLComponent

translate_dict = {
    'AlterTable': 'ALTER TABLE %s',
}


class DefaultTranslator(AbstractTranslator):
    @property
    def dialect(self):
        return 'default'

    def translate(self, ddl_component: DDLComponent):
        pass
