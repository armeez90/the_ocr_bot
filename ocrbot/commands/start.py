from ocrbot.helpers.decorators import send_typing_action
from telegram import Update
from telegram.ext import CallbackContext

@send_typing_action
def start(update:Update,context:CallbackContext):
    """Send a message when the command /start is issued."""
    first=update.effective_user.first_name
    update.message.reply_text('Привет, '+str(first)+' \n\nТеперь Вам не нужно будет набирать текст вручную. Я это сделаю за Вас! \n\nОтправьте чёткий фрагмент акта в несжатом виде для распознавания!',quote=True)
