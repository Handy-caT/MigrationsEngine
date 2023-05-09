from copy import deepcopy

from typing import List

from database.abstract_interpreter import AbstractInterpreter
from database.ddl_base.ddl_components_abstract import DDLComponent
from database.dialects.mysql.mysql_visitor import MySqlVisitor
from database.dialects.mysql.translate_dict import translate_dict_mysql
from database.translator import Translator


class MySqlInterpreter(AbstractInterpreter):

    def __init__(self):
        self.visitor = MySqlVisitor()
        self.translator = Translator(translate_dict=translate_dict_mysql, dialect='mysql')

    def interpret(self, component: DDLComponent):
        copy = deepcopy(component)
        command: List[str] = []
        result: List[str] = []
        ind = False
        stack = []

        for i in copy:
            i.accept(self.visitor)
            if ind:
                while i not in stack[-1]:
                    stack.pop()
                    command.pop()
                ind = False

            if i.is_composite:
                stack.append(i)
                command.append(self.translator.translate(i))
            else:
                command.append(self.translator.translate(i))
                result.append(self.translator.get_command(command))

                command.pop()
                ind = True

        return result
