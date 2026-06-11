import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# تفعيل التسجيل
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# قراءة المتغيرات من البيئة
BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """أمر البداية"""
    await update.message.reply_text(
        '🤖 مرحباً! أنا بوت الذكاء الاصطناعي.\n'
        'استخدم /help لرؤية الأوامر المتاحة.'
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """أمر المساعدة"""
    await update.message.reply_text(
        '📋 الأوامر المتاحة:\n\n'
        '/start - بدء البوت\n'
        '/help - المساعدة\n'
        '/status - حالة البوت\n'
        '/ai [سؤال] - سؤال الذكاء الاصطناعي\n'
        '/image [وصف] - توليد صورة'
    )

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """حالة البوت"""
    await update.message.reply_text('✅ البوت يعمل بكفاءة!')

def main():
    """تشغيل البوت"""
    application = Application.builder().token(BOT_TOKEN).build()
    
    # إضافة المعالجات
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('help', help_command))
    application.add_handler(CommandHandler('status', status))
    
    # تشغيل البوت
    application.run_polling()

if __name__ == '__main__':
    main()
