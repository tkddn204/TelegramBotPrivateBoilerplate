from telegram.ext import CommandHandler, MessageHandler, Filters

from mybot.handlers.commands import Commands
from mybot.handlers.messages import Messages
from mybot.handlers.inlines import Inlines
from mybot.util.logger import log


class Handlers(Commands, Inlines, Messages):
    def __init__(self):
        super(Handlers, self).__init__()
        self._handlers = [
            # Add your Commands, Inlines, Messages!
            CommandHandler('start', self.command_start),
            CommandHandler(['help', 'h'], self.command_help),
            MessageHandler(Filters.text, self.message_handle),
        ]

    def error_handler(self, bot, update, err):
        log.error('%s : ERROR to update :: %s \n %s'
                  % (bot, update, err))

    def get_handlers(self):
        return self._handlers
