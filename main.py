import random
import ptbot

from pytimeparse import parse
from decouple import config


TG_TOKEN = config('TG_TOKEN') 
TG_CHAT_ID = config('TG_CHAT_ID')


def reply(chat_id, message):
    number = parse(message)
    message_id = bot.send_message(chat_id, 'Запускаю таймер')
    bot.create_timer(
        number,
        mailing, 
        chat_id = chat_id, 
        message = message
    )
    bot.create_countdown(
        number, 
        notify_progress,
        chat_id = chat_id, 
        message_id = message_id, 
        number = number
    )   


def mailing (chat_id, message):
    bot.send_message(chat_id, 'Время вышло!')


def notify_progress(secs_left, chat_id, message_id, number):
    bot.update_message(
    chat_id, 
    message_id,
    'Осталось {} секунд\n{}'.format(secs_left, render_progressbar(number, number - secs_left))
    )    


def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)


def main():
    bot.send_message(TG_TOKEN, "Привет!")
    bot.reply_on_message(reply)
    bot.run_bot()


if __name__ == '__main__':
    bot = ptbot.Bot(TG_CHAT_ID)
    main()
    
    
