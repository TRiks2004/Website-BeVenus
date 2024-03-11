from peewee import *

database = PostgresqlDatabase('BeVenus', **{'host': 'localhost', 'port': 6097, 'user': 'postgres', 'password': '4n8Ru5zn6TGQ7RCkaanQ'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Groups(BaseModel):
    created_at = DateTimeField(column_name='created at', constraints=[SQL("DEFAULT now()")])
    id = UUIDField(constraints=[SQL("DEFAULT uuid6()")], primary_key=True)
    name = CharField()

    class Meta:
        table_name = 'groups'

class Todos(BaseModel):
    selected = BooleanField(constraints=[SQL("DEFAULT false")], null=True)
    text = CharField()

    class Meta:
        table_name = 'todos '

class GroupsTodos(BaseModel):
    group = ForeignKeyField(column_name='group', field='id', model=Groups)
    todo = ForeignKeyField(column_name='todo', field='id', model=Todos)

    class Meta:
        table_name = 'groups_todos'
        indexes = (
            (('todo'), True),
        )

class Users(BaseModel):
    email = CharField(unique=True)
    id = UUIDField(constraints=[SQL("DEFAULT uuid6()")], primary_key=True)
    login = CharField(null=True, unique=True)
    password = CharField(null=True)

    class Meta:
        table_name = 'users'

class Spases(BaseModel):
    created_at = DateTimeField(column_name='created at', constraints=[SQL("DEFAULT now()")])
    favorite = BooleanField(constraints=[SQL("DEFAULT false")])
    id = UUIDField(constraints=[SQL("DEFAULT uuid6()")], primary_key=True)
    img = CharField()
    name = CharField()
    user = ForeignKeyField(column_name='user', field='id', model=Users)

    class Meta:
        table_name = 'spases'

class SpasesGroups(BaseModel):
    group = ForeignKeyField(column_name='group', field='id', model=Groups)
    spases = ForeignKeyField(column_name='spases', field='id', model=Spases)

    class Meta:
        table_name = 'spases_groups'
        indexes = (
            (('spases'), True),
        )

