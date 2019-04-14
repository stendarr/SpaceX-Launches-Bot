from src.FormatHTML import strHTML
import logging, os
from src import DictManager, Requests
from telegram import ParseMode
from telegram.ext import Updater, CommandHandler

token = os.environ['TELEGRAM_TOKEN']

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.ERROR)
logger = logging.getLogger(__name__)

def start(bot, update):
    text = "Welcome to the " + strHTML("where's-my-car-bot").makeBold() + "!"
    text += "\n\nIf Elon wants to yeet another car into space, the least you can do is to know when it's happening. Don't miss any of SpaceX's launches with this bot."
    text += "\n\nThere are two commands:\n/next and /last\nglhf."
    bot.send_message(update.message.chat_id, text, parse_mode=ParseMode.HTML)
def info(bot, update):
    text = "Bugs? Suggestions? Need help with your life insurance?\n" + strHTML("Contact Me").addURL("https://odrljin.xyz/#three") + " or visit this project's " + strHTML("GitHub page").addURL("https://github.com/stendarr/SpaceX-Launches-Bot")
    text += "\n\nThere are two commands:\n/next and /last\nglhf."
    bot.send_message(update.message.chat_id, text, parse_mode=ParseMode.HTML)
def next_launch(bot, update):
    text = "🚀 Next Launch:\n" + DictManager.getString(Requests.next_launch())
    bot.send_message(update.message.chat_id, text, parse_mode=ParseMode.HTML)
def latest_launch(bot, update):
    text = "🚀 Latest Launch:\n" + DictManager.getString(Requests.latest_launch())
    bot.send_message(update.message.chat_id, text, parse_mode=ParseMode.HTML)

def main():
    updater = Updater(token)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("info", info))
    dp.add_handler(CommandHandler("help", info))
    dp.add_handler(CommandHandler("next", next_launch))
    dp.add_handler(CommandHandler("last", latest_launch))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
