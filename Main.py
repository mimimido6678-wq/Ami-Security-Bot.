import telebot

# هاد السطر فيه التوكن ديالك اللي خديتي من BotFather
API_KEY = "8677122305:AAHcCJUg8c7pc-Pumxliiaz8zkcleyqzXBE"

bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "مرحباً! أنا بوت الحماية الخاص بك. أنا الآن أعمل مباشرة من السيرفر! 🚀")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"لقد أرسلت: {message.text}")

# هاد السطر كيخلي البوت ديما كيتسنى الرسائل
bot.infinity_polling()
