import telebot
import os

# Create bot
BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

# Add supported commands
@bot.message_handler(commands = ['start','help'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Здравствуйте, я бот-помощник в создании сборок")
    

# Run bot
bot.polling()