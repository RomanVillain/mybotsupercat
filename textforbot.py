from telegram import Update 
from telegram.ext import Updater, Filters, CommandHandler, MessageHandler, CallbackContext 
 
token = "5411812213:AAFo4LzOPhr3_bdZCiTC1ka8heZgzt9y-10" 
updater = Updater(token, use_context=True) 
dispatcher = updater.dispatcher 
 
def start_handler(update: Update, context: CallbackContext): 
    context.bot.send_message(chat_id=update.effective_chat.id,  text=f"Hello, {update.effective_chat.first_name}!") 
 
def message_handler(update: Update, context: CallbackContext): 
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text) 
 
start_command_handler = CommandHandler("start", start_handler) 
dispatcher.add_handler(start_command_handler) 
 
text_handler = MessageHandler(Filters.text & ~Filters.command, message_handler) 
dispatcher.add_handler(text_handler) 
 
# Start bot 
updater.start_polling()