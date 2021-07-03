from peewee import (
    Model,
    CharField,
    PrimaryKeyField,
    DateTimeField,
    MySQLDatabase
)

from app.settings import DB_NAME, USER, PASSWORD

db = MySQLDatabase(
    DB_NAME, user=USER,
    password=PASSWORD,
    host='localhost'
)


class BaseModel(Model):
    class Meta:
        database = db


class Apartment(BaseModel):
    title = CharField(max_length=100)
    location = CharField(max_length=255)
    price = CharField(max_length=20)
    date_time = DateTimeField()

    class Meta:
        db_table = 'apartments'
