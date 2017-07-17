from telegram import ReplyKeyboardMarkup

from .strings import TEXT_START, TEXT_HELP, KEYBOARD_SELECT


class Commands:
    def __init__(self):
        pass

    def command_start(self, bot, update):
        user_name = update.message.from_user.first_name
        chat_id = update.message.chat_id

        bot.sendMessage(chat_id,
            text=TEXT_START.format(
                user_name=user_name, bot_name=bot.name),
            reply_markup=ReplyKeyboardMarkup(KEYBOARD_SELECT))

    def command_help(self, bot, update):
        chat_id = update.message.chat_id

        bot.sendMessage(chat_id,
            text=TEXT_HELP)

    # add def command_foobar
