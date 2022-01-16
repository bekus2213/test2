from peewee import (SqliteDatabase, Model, CharField, TextField)

from config import DB_NAME

db = SqliteDatabase(DB_NAME)


class _Model(Model):
    class Meta:
        database = db


class Users(_Model):
    class Meta:
        db_table = "user"
        indexes = ("username")

    username = CharField(max_length=20, null=False)
