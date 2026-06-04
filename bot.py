import os
import sys
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Setup explicit logging to catch system signals
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends the explicit welcome message to anyone who starts the bot."""
    welcome_message = (
        "Welcome!\n\n"
        "Thanks for joining. Use /start to begin and explore what I can do."
    )
    # Target reply to user chat id directly to handle concurrent interactions
    await update.message.reply_text(text=welcome_message)

def main():
    # Attempt to extract token safely
    TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    
    if not TOKEN:
        logger.critical("FATAL ERROR: TELEGRAM_BOT_TOKEN environment variable is completely missing!")
        sys.exit("Error: Run terminated because TELEGRAM_BOT_TOKEN is not set in Render Environment settings.")

    logger.info("Initializing Telegram Application Instance...")
    application = Application.builder().token(TOKEN).build()

    # Bind the /start command execution
    application.add_handler(CommandHandler("start", start))

    logger.info("Bot successfully linked. Starting background long-polling loop...")
    
    # Run the bot in a continuous blocking loop ideal for background workers
    application.run_polling(drop_pending_updates=True)

if __name__ == '__main__':
    main()
