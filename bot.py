import os
import telebot

# Fetch the token from Render's environment variables
BOT_TOKEN = os.environ.get('BOT_TOKEN')

if not BOT_TOKEN:
    raise ValueError("No BOT_TOKEN found in environment variables!")

bot = telebot.TeleBot(BOT_TOKEN)

# This decorator listens for the /start command from ANY user
@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = (
        "Welcome! This bot helps answer questions and provides useful information. "
        "You can also follow our official channel for updates: https://t.me/GMKChannel"
    )
    # Reply directly to the user who started the bot
    bot.reply_to(message, welcome_text)

if __name__ == "__main__":
    print("Bot is starting up...")
    # non_stop=True ensures the bot stays alive even if it encounters temporary network errors
    bot.infinity_polling(non_stop=True)
