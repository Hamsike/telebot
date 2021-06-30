import datetime

import telebot as tb
import datetime as dt
from pyowm import OWM
import logging, time, sys

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
        city = message.text[9:]
        if city:
            owm = OWM('3bf8a370a9cffee5cfaf28c2250f6f5e', language='RU')
            weather = owm.weather_at_place(city)
            status = ''
            vetr = ''
            obs = weather.get_weather()
            if obs.get_status() == 'Clear':
                status = 'Безоблачно'
            if obs.get_status() == 'Clouds':
                status = 'Облачно'
            if obs.get_status() == 'Rain':
                status = 'Дождь'
            if obs.get_status() == 'Sun':
                status = 'Солнечно'
            try:
                if 348.75 < obs.get_wind()['deg'] <= 360 or 360 < obs.get_wind()['deg'] <= 11.25:
                    vetr = 'Северный'
                if 11.25 < obs.get_wind()['deg'] <= 78.75:
                    vetr = 'Северо-Восточный'
                if 78.75 < obs.get_wind()['deg'] <= 101.25:
                    vetr = 'Восточный'
                if 101.75 < obs.get_wind()['deg'] <= 168.75:
                    vetr = 'Юго-Восточный'
                if 168.75 < obs.get_wind()['deg'] <= 191.75:
                    vetr = 'Южный'
                if 191.75 < obs.get_wind()['deg'] <= 258.75:
                    vetr = 'Юго-Западный'
                if 258.75 < obs.get_wind()['deg'] <= 281.25:
                    vetr = 'Западный'
                if 281.25 < obs.get_wind()['deg'] <= 348.75:
                    vetr = 'Северо-Западный'
            except KeyError:
                vetr = 'Нет данных'
            temp = f"Температура: {obs.get_temperature('celsius')['temp']}\n" \
                   f"Статус: {status}\n" \
                   f"Ветер💨: Направление: {vetr}\n                  Скорость: {obs.get_wind()['speed']} м/с\n" \
                   f"Влажность💦: {obs.get_humidity()}"
            bot.send_message(message.chat.id, temp)
        else:
            bot.send_message(message.chat.id, 'Введите строку типа /weather {город}')


while True:
    try:
        bot.polling(none_stop=True)
    except TypeError:
        logging.error('error: {}'.format(sys.exc_info()[0]))
        time.sleep(5)
