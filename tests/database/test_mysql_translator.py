def test_composite_alter_column_translate(composite_ddl, mysql_translator, mysql_visitor):
    result = []

    for component_node in composite_ddl:
        component_node.accept(mysql_visitor)
        result.append(mysql_translator.translate(component_node))

    assert result == [
        '',
        'ALTER TABLE users',
        'MODIFY COLUMN password varchar(40)',
        'DEFAULT xd',
        'NOT NULL',
        '',
        'SHOW COLUMNS FROM users',
        ]
