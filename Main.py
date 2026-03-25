import telebot
from telebot import types

# حط التوكن ديالك هنا
API_TOKEN = 'YOUR_BOT_TOKEN_HERE'

bot = telebot.TeleBot(API_TOKEN)

# دالة الترحيب والأزرار الرئيسية
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    
    btn1 = types.InlineKeyboardButton("🤝 إنشاء صفقة جديدة", callback_data="create_deal")
    btn2 = types.InlineKeyboardButton("📊 صفقاتي", callback_data="my_deals")
    btn3 = types.InlineKeyboardButton("👨‍💻 الدعم الفني", callback_data="support")
    btn4 = types.InlineKeyboardButton("📢 قناة الإثباتات", url="https://t.me/your_channel") # حط رابط قناتك هنا
    
    markup.add(btn1, btn2, btn3, btn4)
    
    welcome_text = (
        "🛡️ **مرحباً بك في Ami Security**\n\n"
        "الوسيط الرقمي الموثوق لضمان حقك في كاع المعاملات.\n\n"
        f"🆔 الـ ID ديالك هو: `{message.from_user.id}`\n"
        "👇 اختار شنو بغيتي دير دابا:"
    )
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup, parse_mode="Markdown")

# هاد الجزء هو اللي كيعالج ضغطات الأزرار (اللي كان ناقصك)
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == "create_deal":
        # هنا البوت غيجاوبك ملي تضغط على إنشاء صفقة
        bot.answer_callback_query(call.id) # باش تحيد ديك الدويرة اللي كتدور فوق الزر
        msg = bot.send_message(call.message.chat.id, "📝 **وصف الخدمة:**\nصيفط ليا دابا شنو هي الخدمة اللي بغيتي تشريه أو تبيعها (مثلاً: شراء حساب تيك توك).")
        bot.register_next_step_handler(msg, process_description_step)
        
    elif call.data == "my_deals":
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "📦 ما عندك حتى شي صفقة حالياً.")
        
    elif call.data == "support":
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, "👨‍💻 تواصل مع الإدارة هنا: @YourAdminUsername")

# دالة لاستلام وصف الخدمة (مثال بسيط)
def process_description_step(message):
    service_desc = message.text
    bot.send_message(message.chat.id, f"✅ تم تسجيل الوصف: {service_desc}\nقريباً غانزيدو كود تحديد الثمن.")

# تشغيل البوت
if __name__ == "__main__":
    print("Bot is starting...")
    bot.infinity_polling()
