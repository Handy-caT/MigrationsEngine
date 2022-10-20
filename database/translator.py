from database.ddl_base.ddl_components_abstract import DDLComponent


def _get_command(command: list[str]) -> str:
    return (' '.join(command).strip() + ';')


class Translator:
    @property
    def dialect(self):
        return 'default'

    def __init__(self, translate_dict: dict):
        self.translate_dict = translate_dict

    def _translate_one(self, component: DDLComponent):
        return self.translate_dict[component.__class__.__name__](component)

    def translate(self, ddl_component: DDLComponent):
        command = []
        depth = 0
        result = []

        for i in ddl_component:
            if i[1] > depth:
                depth += 1
            else:
                while len(command) > i[1]:
                    command.pop()

            if i[0].is_composite:
                command.append(self._translate_one(i[0]))
            else:
                command.append(self._translate_one(i[0]))
                result.append(_get_command(command))

        return result
