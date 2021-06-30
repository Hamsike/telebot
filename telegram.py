import datetime

import telebot as tb
import datetime as dt
import requests

f = {
    '01': 'Января', '02': 'Февраля', '03': 'Марта', '04': 'Апреля', '05': 'Мая', '06': 'Июня',
    '07': 'Июля', '08': 'Августа', '09': 'Сентября', '10': 'Октября', '11': 'Ноября', '12': 'Декабря'
}
bot = tb.TeleBot('1720964485:AAEjzAL1d-49427Z0W560_7TniBEkyrwguo')


class Tele:
    @staticmethod
    @bot.message_handler(commands='start')
    def start_command(message):
        bot.send_message(message.chat.id, "Hello!")

    @staticmethod
    @bot.message_handler(commands='time')
    def time(message):
        d = dt.date.today().isoformat().split('-')
        t = dt.datetime.today().time().isoformat().split(':')
        date = f'Дата: {d[2]} {f[d[1]]} {d[0]} года\nВремя: {t[0]}:{t[1]}'
        bot.send_message(message.chat.id, date)

    @staticmethod
    @bot.message_handler(commands='weather')
    def weather(message):
        ctx = message.text[7:]
        if ctx:
            print(bot.get_my_commands())


bot.polling()
