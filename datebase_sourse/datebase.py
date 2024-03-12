from peewee import PostgresqlDatabase, Model

database = PostgresqlDatabase('BeVenus', **{'host': 'app_postgres', 'port': 5432, 'user': 'postgres', 'password': '4n8Ru5zn6TGQ7RCkaanQ'})

class BaseModel(Model):
    class Meta:
        database = database