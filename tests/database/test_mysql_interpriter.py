from database.dialects.mysql.mysql_interpreter import MySqlInterpreter


def test_mysql_interpreter(composite_ddl):
    interpreter = MySqlInterpreter()
    assert interpreter.interpret(composite_ddl) == [
        'ALTER TABLE users MODIFY COLUMN password varchar(40) DEFAULT xd NOT NULL;',
        'SHOW COLUMNS FROM users;'
    ]
