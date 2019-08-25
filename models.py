from peewee import *
from flask_login import UserMixin
import datetime

DATABASE = SqliteDatabase('clientsss.sqlite')


class User(UserMixin, Model):
    id = IntegerField(primary_key=True)
    username = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField()

    class Meta:
        database = DATABASE

class Client(Model):
    owner = CharField()
    price = FloatField()
    description = CharField()
    image = CharField()
    user = ForeignKeyField(User, backref="clients")
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User, Client], safe=True)
    print("TABLES CREATED")
    DATABASE.close()

