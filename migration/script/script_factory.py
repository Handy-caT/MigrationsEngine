from database.ddl_base.ddl_components_abstract import DDLComponent


class ScriptFactory:
    def __init__(self, path: str):
        self.path = path

    def get_commands(self, component: DDLComponent) -> list[str]:
        component_string = component.__repr__()

