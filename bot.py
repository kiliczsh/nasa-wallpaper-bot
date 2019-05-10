from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
from os import environ

def get_image_url():
    API_KEY = environ.get('NASA_API_KEY')
    base_url = str('https://api.nasa.gov/planetary/apod?api_key='+API_KEY)
    data = requests.get(base_url).json()
    url = data['url']
    return url

def picture(bot, update):
    image_url = get_image_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=image_url)

def main():
    print("Visit t.me/nasawallbot :) ")
    BOT_API_KEY= str(environ.get('TELEGRAM_BOT_API_KEY'))
    updater = Updater(BOT_API_KEY)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('picture',picture))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()