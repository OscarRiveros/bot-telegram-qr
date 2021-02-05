import os
import sys
import logging
import qrcode
from telegram import Update
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters
from telegram import ChatAction
INPUT_TEXT = 0


# Enable logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s,")
logger = logging.getLogger()

mode  = os.getenv('MODE')
def start(update, context):
        text='Enviame un texto para generar codigo QR ')
    return INPUT_TEXT
    logger.info(f"El usuario {update.effective_user['username']}, ha inicadio una conversacion")
    nombre = update.effective_user['first_name']
    update.message.reply_text(f"Hola {nombre}, bienvenido al BOT DE Don Cañete\n\nEste es un texto pre definido, que quieres hacer?\n\nEsto son algunos comandos\n1- /qr generar codigo QR")


def run(updater):
    PORT = int(os.environ.get("PORT", "8443"))
    HEROKU_APP_NAME = os.environ.get("bot-telegram-qr")
    updater.start_webhook(listen='0.0.0.0',
                      port=PORT,
                      url_path='1493285499:AAEpQ8ajsD_NFjyX4RXwUc3UvRRZmwC4vsA')
    updater.bot.set_webhook("https://{bot-telegram-qr.herokuapp}.herokuapp.com/{TOKEN}")

def texto_command_handler(update, context):
    
    update.message.reply_text(
        text='Enviame un texto para generar codigo QR ')
    return INPUT_TEXT

def generate_qr(texto):
    
    filename= texto + '.jpg'
    #hola.jpg
    img = qrcode.make(texto)
    img.save(filename)
    
    return filename

def send_qr(filename, chat):
    chat.send_action(
        action=ChatAction.UPLOAD_PHOTO,
        timeout=None
    )
    chat.send_photo(
        photo=open(filename, 'rb')
    )
    os.unlink(filename)

def input_text(update, context):
    
    texto = update.message.text
    filename = generate_qr(texto)
    chat = update.message.chat
    send_qr(filename, chat)
    return ConversationHandler.END

def dialogo(update, context):
    user_id = update.effective_user['id']
    nombre = update.effective_user['first_name']
    logger.info(f'El usuario {user_id}, ha enviado un mensaje de texto')
    text = update.message.text
    context.bot.sendMessage(
        chat_id=user_id,
        
        text = f'*{nombre}* Escribio:\n{text}'
    )

if __name__ == '__main__':

    updater = Updater(token='1493285499:AAEpQ8ajsD_NFjyX4RXwUc3UvRRZmwC4vsA', use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(ConversationHandler(
        entry_points=[
            CommandHandler('qr', texto_command_handler)
        ],

        states={
            INPUT_TEXT : [MessageHandler(Filters.text, input_text)]
        },

        fallbacks=[],
    ))
    dp.add_handler(MessageHandler(Filters.text, dialogo))
    
    run(updater)
    updater.start_polling()
    print('BOT INICIADOO')
    updater.idle()

