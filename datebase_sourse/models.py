from peewee import *
from playhouse.postgres_ext import *

from .datebase import BaseModel

class UnknownField(object):
    def __init__(self, *_, **__): pass



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
    way = CharField(null=True)

    class Meta:
        table_name = 'spases'

class Groups(BaseModel):
    created_at = DateTimeField(column_name='created at', constraints=[SQL("DEFAULT now()")])
    id = UUIDField(constraints=[SQL("DEFAULT uuid6()")], primary_key=True)
    name = CharField()
    spase = ForeignKeyField(column_name='spase', field='id', model=Spases)

    class Meta:
        table_name = 'groups'

class Todos(BaseModel):
    group = ForeignKeyField(column_name='group', field='id', model=Groups)
    selected = BooleanField(constraints=[SQL("DEFAULT false")], null=True)
    text = CharField()

    class Meta:
        table_name = 'todos'

class Token(BaseModel):
    browser = CharField()
    created_at = DateTimeField(constraints=[SQL("DEFAULT now()")])
    device = CharField()
    live = IntervalField(constraints=[SQL("DEFAULT '1 day'::interval")])  # interval
    token = UUIDField(constraints=[SQL("DEFAULT uuid6()")], primary_key=True)
    user = ForeignKeyField(column_name='user', field='id', model=Users)

    class Meta:
        table_name = 'token'

