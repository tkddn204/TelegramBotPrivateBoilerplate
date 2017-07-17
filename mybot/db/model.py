from .use_peewee import *


class BaseModel(Model):
    class Meta:
        database = bot_database

# Make your DB Model!
class MyBotModel(BaseModel):
    bot_name = CharField(max_length=20, null=False, default='MyBot')
    bot_age = IntegerField()
    tell_the_bot = TextField()
