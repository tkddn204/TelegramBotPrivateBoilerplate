# If you use Messages, modify this.
import re

from telegram import InlineKeyboardMarkup, InlineKeyboardButton


class Messages:
    def __init__(self):
        pass

    def message_handle(self, bot, update):
        text = update.message.text
        regex_text = re.compile("wow").search(text)

        if regex_text:
            regex_text = regex_text.group()
            chat_id = update.message.chat_id
            wait_message = bot.sendMessage(chat_id,
                                           text="amazing!")
        else:
            pass
