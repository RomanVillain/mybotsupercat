import telegram
from telegram import Update,ChatAction
from telegram.ext import Updater,Filters,CommandHandler,MessageHandler,CallbackContext
# from telebot import ChatAction
bot = token = "5411812213:AAFo4LzOPhr3_bdZCiTC1ka8heZgzt9y-10" 


updater = Updater(token, use_context=True) 
dispatcher = updater.dispatcher 

def start_handler(update: Update, context: CallbackContext): 
    context.bot.send_message(chat_id=update.effective_chat.id,  text=f"Hello, {update.effective_chat.first_name}!") 
 
start_command_handler = CommandHandler("start", start_handler) 
dispatcher.add_handler(start_command_handler) 

def help_command_handler(update: Update, context: CallbackContext):
    with open('clinteastwood4eel.png', 'rb') as file:
        context.bot.send_chat_action(update.effective_chat.id, ChatAction.UPLOAD_PHOTO)
        context.bot.send_photo(update.effective_chat.id, photo=file)

help_handler = CommandHandler('help', help_command_handler)
dispatcher.add_handler(help_handler)



# Запуск бота 
updater.start_polling()
