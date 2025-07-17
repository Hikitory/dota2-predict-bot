# main.py
import logging
from telegram import Bot
from telegram.ext import Updater, CommandHandler

TOKEN = 'твой_токен_бота'

def start(update, context):
    update.message.reply_text("Привет! Я Dota 2 аналитик!")

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
