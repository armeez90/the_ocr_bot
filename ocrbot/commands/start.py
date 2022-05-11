from ocrbot.helpers.decorators import send_typing_action
from telegram import Update
from telegram.ext import CallbackContext

@send_typing_action
def start(update:Update,context:CallbackContext):
    """Send a message when the command /start is issued."""
    first=update.effective_user.first_name
    update.message.reply_text('Здравствуйте, '+str(first)+' \n\nТеперь Вам не нужно набирать текст вручную. Я это сделаю за Вас! \n\nОтправьте читабельный фрагмент акта в сжатом виде для распознавания!',quote=True)
