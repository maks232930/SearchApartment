# auto-generated snapshot
from peewee import *
import datetime
import peewee


snapshot = Snapshot()


@snapshot.append
class Apartment(peewee.Model):
    title = CharField(max_length=100)
    location = CharField(max_length=255)
    price = CharField(max_length=20)
    date_time = DateTimeField()
    class Meta:
        table_name = "apartments"


