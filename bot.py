import telebot
import random
import os

# گرفتن توکن از محیط
TOKEN = os.getenv('BOT_TOKEN')

bot = telebot.TeleBot(TOKEN)

# لیست استیکرها
stickers = [
    'CAACAgUAAxkBAAEDq19lpsk1xyz',
    'CAACAgUAAxkBAAEDq2Blpsk7fgh',
]

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text.lower()
    
    if "بغل" in text:
        bot.send_sticker(message.chat.id, random.choice(stickers))
        bot.send_message(message.chat.id, "محکم بغلت کردم عشقم!")
    elif "بوس" in text:
        bot.send_sticker(message.chat.id, random.choice(stickers))
        bot.send_message(message.chat.id, "یه بوس خوشمزه برات فرستادم!")
    else:
        bot.send_message(message.chat.id, "دوست دارم قند عسلم!")

bot.polling()