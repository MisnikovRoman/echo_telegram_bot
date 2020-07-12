import telebot

bot = telebot.TeleBot("TOKEN")

@bot.message_handler(commands = ['start','help'])
def send_welcome(message):
    bot.reply_to(message, message.text)


bot.polling()
