from src.FormatHTML import strHTML
import logging, os
from src import DictManager, Requests
from telegram import ParseMode
from telegram.ext import Updater, CommandHandler


with open('token', 'r') as content_file:
    token = content_file.read().strip()

# If you want to use environment variables for use with docker, uncomment this line
# token = os.environ['TELEGRAM_TOKEN']

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.ERROR)
logger = logging.getLogger(__name__)

def start(bot, update):
    text = "Welcome to the " + strHTML("where's-my-car-bot").makeBold() + "!"
    text += "\n\nIf Elon wants to yeet another car into space, the least you can do is to know when it's happening. Don't miss any of SpaceX's launches with this bot."
    text += "\n\nThere are two commands:\n/next and /last\nglhf."
    bot.send_message(update.message.chat_id, text, parse_mode=ParseMode.HTML)
def info(bot, update):
    text = "Bugs? Suggestions? Need help with your life insurance?\n" + strHTML("Contact Me").addURL("https://odrljin.xyz/#three") + " or visit this project's " + strHTML("GitHub page").addURL("https://github.com/stendarr/wheresmycar-bot")
    text += "\n\nThere are two commands:\n/next and /last\nglhf."
    bot.send_message(update.message.chat_id, text, parse_mode=ParseMode.HTML)
def next_launch(bot, update):
    text = "🚀 Next Launch:\n" + DictManager.getString(Requests.next_launch())
    bot.send_message(update.message.chat_id, text, parse_mode=ParseMode.HTML)
def latest_launch(bot, update):
    text = "🚀 Latest Launch:\n" + DictManager.getString(Requests.latest_launch())
    bot.send_message(update.message.chat_id, text, parse_mode=ParseMode.HTML)
def wheresmycar(bot,update):
    text = "Your car is parked " + strHTML("here").addURL("https://www.whereisroadster.com/")
    bot.send_message(update.message.chat_id, text, parse_mode=ParseMode.HTML)

def sub(bot,update):
    chat_id = str(update.message.chat_id)
    subscribers = []
    f = open("subs", "r")
    for line in f:
        subscribers.append(line.strip())
    f.close()

    if chat_id in subscribers:
        bot.send_message(update.message.chat_id, "Already subscribed", parse_mode=ParseMode.HTML)
    else:
        f = open("subs","a")
        f.write("\n"+chat_id)
        f.close()
        bot.send_message(update.message.chat_id, "Subscribed.", parse_mode=ParseMode.HTML)

def unsub(bot,update):
    chat_id = str(update.message.chat_id)
    subscribers = []
    f = open("subs", "r")
    for line in f:
        subscribers.append(line.strip())
    f.close()

    for i in subscribers:
        if chat_id in i:
            subscribers.remove(i)

    with open('subs', 'w') as f:
        for item in subscribers:
            if item.strip()!="":
                f.write("%s\n" % item)

    bot.send_message(update.message.chat_id, "Unsubscribed.", parse_mode=ParseMode.HTML)

def main():
    updater = Updater(token)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("info", info))
    dp.add_handler(CommandHandler("help", info))
    dp.add_handler(CommandHandler("next", next_launch))
    dp.add_handler(CommandHandler("last", latest_launch))
    dp.add_handler(CommandHandler("dude", wheresmycar))
    dp.add_handler(CommandHandler("wheresmycar", wheresmycar))
    dp.add_handler(CommandHandler("sub", sub))
    dp.add_handler(CommandHandler("unsub", unsub))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
