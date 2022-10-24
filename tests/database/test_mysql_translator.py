def test_composite_alter_column_translate(composite_ddl, mysql_translator, mysql_visitor):

    for component_node in composite_ddl:
        component_node[0].accept(mysql_visitor)

    assert mysql_translator.translate(composite_ddl) == [
        'ALTER TABLE users MODIFY COLUMN password varchar(40) DEFAULT xd NOT NULL;',
        'SHOW COLUMNS FROM users;'
    ]
