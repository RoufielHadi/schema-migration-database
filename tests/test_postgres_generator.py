from src.ast.models import Schema, Table, Column
from src.generator.PostgreSQLGenerator import PostgreSQLGenerator


def test_create_table_contains_primary_key():
    users = Table(name='users', columns=[
        Column(name='id', type='int', primary=True),
        Column(name='email', type='varchar', length=120, not_null=True),
    ])
    schema = Schema(name='shop', tables=[users])
    gen = PostgreSQLGenerator(schema)
    sql = gen.create_table(users)
    assert 'CREATE TABLE IF NOT EXISTS "shop"."users"' in sql
    assert '"id" int PRIMARY KEY' in sql
    assert '"email" varchar(120) NOT NULL' in sql
