import telebot
import os

# Create bot
BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

# Add supported commands
@bot.message_handler(commands = ['start','help'])
def send_welcome(message):
    bot.reply_to(message, "Здравствуйте, я бот помощник в создании сборок")

# Run bot
bot.polling()