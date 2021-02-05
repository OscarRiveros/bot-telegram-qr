import os
import sys
import logging
import telegram
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


# Enable logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s,")

logger = logging.getLogger()
TOKEN = os.environ['TOKEN']
print('tokennn ',TOKEN)

#or9av8la7;co

    