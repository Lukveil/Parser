from peewee import IntegerField, CharField, Model, SqliteDatabase, DateTimeField, PrimaryKeyField

db = SqliteDatabase('log_db.db')

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    id = IntegerField(primary_key=True)
    day = IntegerField(default=None)
    time = DateTimeField(default=None)
    user = IntegerField(default=None)
    team = IntegerField(default=None)
    project = IntegerField(default=None)
    version = IntegerField(default=None)
    operate = CharField(default=None)

db.create_tables(BaseModel.__subclasses__())


