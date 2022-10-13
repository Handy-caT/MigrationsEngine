from database.abstract_translator import AbstractTranslator
from database.ddl_base.ddl_components_abstract import DDLComponent


class MySqlTranslator(AbstractTranslator):
    @property
    def dialect(self):
        return 'mysql'

    def translate(self, ddl_component: DDLComponent):
        pass
    