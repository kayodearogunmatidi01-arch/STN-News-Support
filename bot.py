import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Enable logging so you can see what's happening in your Render logs
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Define the /start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # This sends the message to anyone who triggers the /start command
    welcome_message = (
        "Welcome!\n\n"
        "Thanks for joining. Use /start to begin and explore what I can do."
    )
    await update.message.reply_text(welcome_message)

def main():
    # Grab the token from Render's Environment Variables
    TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
    
    if not TOKEN:
        logger.error("No token found! Make sure TELEGRAM_BOT_TOKEN is set in Render.")
        return

    # Build the application
    application = Application.builder().token(TOKEN).build()

    # Register the /start command
    application.add_handler(CommandHandler("start", start))

    # Run the bot using polling (perfect for a background worker)
    logger.info("Bot is starting...")
    application.run_polling()

if __name__ == '__main__':
    main()
