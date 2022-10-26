from copy import deepcopy

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
        for component in copy:
            component[0].accept(self.visitor)

        return self.translator.translate(copy)
