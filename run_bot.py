import os 
import telebot

API_KEY = os.getenv('API_KEY', 'value does not exist')
# API_KEY = '2084572224:AAEWPqcQk9B61cR0jECPuX4IgDsJzJrlWAw/'
print(API_KEY)
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['hello'])
def hello(message):
    bot.send_message(message.chat.id, 'Hello!')

bot.polling()
