from .use_peewee import bot_database
from .model import MyBotModel


class BotDB:
    def __init__(self):
        bot_database.get_conn()
        bot_database.create_tables([MyBotModel], safe=True)

    @staticmethod
    def get_my_bot_model():
        return MyBotModel.select().get()

    # Write this area your get/set db queries!
