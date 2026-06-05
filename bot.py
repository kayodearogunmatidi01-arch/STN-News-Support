import os
import logging
import asyncio
import nest_asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Apply the nested async patch for background environments
nest_asyncio.apply()

# Setup logging to Render dashboard
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# /start command logic
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    welcome_message = (
        "Welcome!\n\n"
        "Thanks for joining. Use /start to begin and explore what I can do."
    )
    logger.info(f"User {update.effective_user.id} started the bot.")
    await update.message.reply_text(welcome_message)

async def main():
    TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
    
    if not TOKEN:
        logger.error("CRITICAL: TELEGRAM_BOT_TOKEN is missing in Render environment variables!")
        return

    logger.info("Initializing Telegram Bot Application...")
    application = Application.builder().token(TOKEN).build()

    # Register the start handler
    application.add_handler(CommandHandler("start", start))

    # Initialize and start polling explicitly for background tasks
    await application.initialize()
    await application.start()
    
    logger.info("Bot is successfully polling Telegram servers...")
    await application.updater.start_polling(allowed_updates=Update.ALL_TYPES)
    
    # Keeps the loop running indefinitely on the Render Background Worker
    while True:
        await asyncio.sleep(3600)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("Bot stopped.")
