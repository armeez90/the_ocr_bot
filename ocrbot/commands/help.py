from telegram import Update
from telegram.ext import CallbackContext
from ocrbot.helpers.decorators import send_typing_action

@send_typing_action
def help(update:Update,context:CallbackContext):
    """Send a message when the command /help is issued."""
    update.message.reply_text(
        "Доступный список команд:\
        \n/start - Запустить бота\
        \n/help - Показать это сообщение",quote=True
    )
