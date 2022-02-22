from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext


def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')


updater = Updater('5225133655:AAGV10r8vme0VoxrXQco2OQLNs7FF4xe3u8')

updater.dispatcher.add_handler(CommandHandler('hello', hello))
print('here we go')
updater.start_polling()
updater.idle()