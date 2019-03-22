from src.FormatHTML import strHTML
import logging, os
from src import DictManager, Requests
from telegram import ParseMode
from telegram.ext import Updater, CommandHandler

token = os.environ['TELEGRAM_TOKEN']

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def start(bot, update):
    text = "Welcome to the " + strHTML("SpaceX Launches Bot").makeBold() + "!"
    bot.send_message(update.message.chat_id, text, parse_mode=ParseMode.HTML)
def info(bot, update):
    text = "Bugs? Suggestions?\n\n" + strHTML("Contact me :)").addURL("https://t.me/matteomeneghetti")
    bot.send_message(update.message.chat_id, text, parse_mode=ParseMode.HTML)
def next_launch(bot, update):
    text = "🚀 Next launch:\n" + DictManager.getString(Requests.next_launch())
    bot.send_message(update.message.chat_id, text, parse_mode=ParseMode.HTML)
def latest_launch(bot, update):
    text = "🚀 Latest launch:\n" + DictManager.getString(Requests.latest_launch())
    bot.send_message(update.message.chat_id, text, parse_mode=ParseMode.HTML)

def main():
    updater = Updater(token)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("info", info))
    dp.add_handler(CommandHandler("next", next_launch))
    dp.add_handler(CommandHandler("last", latest_launch))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
