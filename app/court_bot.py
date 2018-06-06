# Done! Congratulations on your new bot. You will find it at
#
# t.me/kenya_court_bot.
#
# You can now add a description, about section and profile picture for your bot,
# see /help for a list of commands. By the way, when you've finished creating your cool bot,
# ping our Bot Support if you want a better username for it.
# Just make sure the bot is fully operational before you do this.
#
# Use this token to access the HTTP API:
# 599925015:AAH7DJ2K9719yCLsyowc4WeIZa5KtsIngrM
#
# For a description of the Bot API, see this page: https://core.telegram.org/bots/api

import logging
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters



logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
logger = logging.getLogger(__name__)


# Bot Housekeeping
updater = Updater(token='599925015:AAH7DJ2K9719yCLsyowc4WeIZa5KtsIngrM')
dispatcher = updater.dispatcher

# Now the Bot commands

# Start
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Hi, I am the Kenya Judiciary Bot")
    
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


#Echo
def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)
    
echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)


## Echo in Caps
def caps(bot, update, args):
    text_caps = ' '.join(args).upper()
    bot.send_message(chat_id=update.message.chat_id, text=text_caps)

caps_handler = CommandHandler('caps', caps, pass_args=True)
dispatcher.add_handler(caps_handler)


# Error handler
def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)
    
dispatcher.add_error_handler(error)

# Default Handler
def unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.")

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)


# Start the bot
updater.start_polling()
updater.idle()
# Stop the bot
# updater.stop()