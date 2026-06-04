import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Enable logging to see what's happening in the Render logs
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Define the /start command response
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    welcome_message = (
        "Welcome!\n\n"
        "Thanks for joining. Use /start to begin and explore what I can do."
    )
    # This sends the message back to whoever triggered the command
    await update.message.reply_text(welcome_message)

def main():
    # Fetch the token from Render's environment variables
    TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
    
    if not TOKEN:
        logger.error("No bot token found! Make sure TELEGRAM_BOT_TOKEN is set in Render.")
        return

    # Build the application
    application = Application.builder().token(TOKEN).build()

    # Register the /start command handler
    application.add_handler(CommandHandler("start", start))

    # Start the bot using Long Polling (ideal for Background Workers)
    logger.info("Bot is starting...")
    application.run_polling()

if __name__ == '__main__':
    main()
