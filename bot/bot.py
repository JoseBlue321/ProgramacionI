from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def start(update, context):
    update.message.reply_text('¡Hola! Soy tu bot de Telegram.')

def help_command(update, context):
    update.message.reply_text('Escribe /start para comenzar.')

def echo(update, context):
    update.message.reply_text(update.message.text)

def main():
    updater = Updater("TU_TOKEN_AQUI", use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()