from database.ddl_base.ddl_components_abstract import DDLComponent


class Translator:

    def __init__(self, translate_dict: dict, dialect: str = 'default'):
        self.translate_dict = translate_dict
        self.dialect = dialect

    def translate(self, component: DDLComponent) -> str:
        return self.translate_dict[component.__class__.__name__](component)

    @staticmethod
    def get_command(command: list[str]) -> str:
        return ' '.join(command).strip() + ';'
