# python PogodaTelegramBot.py

import pyowm
import telebot

#owm = pyowm.OWM('a2796b736dbdd2d94dd087be1702d1da', language = "ru")
bot = telebot.TeleBot("927570306:AAFGbFphrT6wzo9hFLRi5dH85xTRehZDWz0")

server = Flask(__name__)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.send_message(message.chat.id, "Введите город")

@bot.message_handler(content_types=['text'])
def send_echo(message):
	place = message.text
	if message.text != place:
		bot.send_message(message.chat.id, "ОШИБКА")
	if message.text == place:
		owm = pyowm.OWM('a2796b736dbdd2d94dd087be1702d1da', language = "ru")
		observation = owm.weather_at_place(message.text)
		w = observation.get_weather()
		temp = w.get_temperature('celsius')["temp"]

		answer = "В городе " + message.text + " сейчас " + w.get_detailed_status() + '\n'
		answer += "Температура " + str(temp) + "°C" + "\n\n"
		bot.send_message(message.chat.id, answer)

		city = "Введите город" + "\n\n"
		bot.send_message(message.chat.id, city)

    if __name__ == '__main__':
        server.debug = True
        server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))

bot.polling(none_stop = True)