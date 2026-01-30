import os
import random
import ptbot

from pytimeparse import parse
from dotenv import load_dotenv 


load_dotenv()
TG_TOKEN = os.getenv('TG_TOKEN') 
TG_CHAT_ID = os.getenv('TG_CHAT_ID')

bot = ptbot.Bot(TG_CHAT_ID)
bot.send_message(TG_TOKEN, "Привет!")
#bot.send_message(TG_TOKEN, "Как дела?")


def wait(chat_id, message):
    number = parse(message)
    bot.create_timer(number, mirror, chat_id = chat_id, message = message)
    counting = bot.create_countdown(number, notify_progress)


def mirror (chat_id, message):
    bot.send_message(chat_id, 'Время вышло!')
    print("Мне написал пользователь с ID:", chat_id)


def notify_progress(secs_left, chat_id, message):
    print('Осталось {} секунд'.format(secs_left))


bot.reply_on_message(chat_id, notify_progress)
bot.reply_on_message(wait)

bot.run_bot()

