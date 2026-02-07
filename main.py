import os
import random
import ptbot

from pytimeparse import parse
from dotenv import load_dotenv 


load_dotenv()
TG_TOKEN = os.getenv('TG_TOKEN') 
TG_CHAT_ID = os.getenv('TG_CHAT_ID')




def wait(chat_id, message):
    number = parse(message)
    message_id = bot.send_message(TG_TOKEN, "Запускаю таймер")
    bot.create_timer(number, mirror, chat_id = chat_id, message = message)
    bot.create_countdown(number, notify_progress, chat_id = chat_id, message_id = message_id)
    



def mirror (chat_id, message):
    bot.send_message(chat_id, 'Время вышло!')
    print("Мне написал пользователь с ID:", chat_id)




def notify_progress(secs_left, chat_id, message_id):
    bot.update_message(chat_id, message_id, 'Осталось {} секунд\n'.format(secs_left), render_progressbar(secs_left, 1))
    


def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)



bot = ptbot.Bot(TG_CHAT_ID)
bot.send_message(TG_TOKEN, "Привет!")
bot.reply_on_message(wait)
bot.run_bot()

