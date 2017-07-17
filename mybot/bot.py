#-*- coding: utf-8 -*-
from telegram.ext import Updater

from .db.botdb import BotDB
from .handlers.handlers import Handlers

from .util.config import TOKEN
from .util.logger import log


def add_handlers(dp):
    handlers = Handlers()
    for handler in handlers.get_handlers():
        dp.add_handler(handler)
    dp.add_error_handler(handlers.error_handler)


def main():
    log.info("Bot is setting...")

    updater = Updater(token=TOKEN)
    dp = updater.dispatcher
    add_handlers(dp)

    # initializing DB
    BotDB().__init__()

    updater.start_polling()
    log.info("Bot starts polling!")
    updater.idle()
