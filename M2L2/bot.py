import telebot
from config import TOKEN
from random import choice
import os 

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def say_hello(message):
    bot.send_message(message.chat.id, "Use the command /meme")

@bot.message_handler(commands=["meme"])
def send_meme(message):
    img_rand = choice(os.listdir("img"))
    with open(f'img/{img_rand}', 'rb') as photo:
        bot.send_photo(message.chat.id, photo)

bot.infinity_polling()