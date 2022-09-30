import sqlalchemy

from migration.sql_alchemy_schema_parser import SQLAlchemySchemaParser


def test_parse_column():
    parser = SQLAlchemySchemaParser()
    column = parser.parse_column(sqlalchemy.schema.Column('id', sqlalchemy.Integer))
    assert column.name == 'id'
    assert column.column_type == 'integer'
    assert column.default is None
    assert column.not_null is False
    assert column.foreign_key is None
    assert column.key is None
