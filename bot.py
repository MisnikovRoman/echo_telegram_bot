import telebot
import os

# Create bot
BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

# Add supported commands
@bot.message_handler(commands = ['start','help'])
def send_welcome(message):
    bot.send_message(message.chat_id, "Здравствуйте, я бот-помощник в создании сборок")
    message

# Run bot
bot.polling()