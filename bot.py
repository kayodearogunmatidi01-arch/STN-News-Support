import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Enable logging so you can see errors on Render
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Sends the welcome message when the command /start is issued."""
    welcome_message = (
        "Welcome!\n\n"
        "Thanks for joining. Use /start to begin and explore what I can do."
    )
    # This sends the message back to whoever triggered the command
    await update.message.reply_text(welcome_message)

def main():
    # Get the token from Render's environment variables (secure)
    TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    
    if not TOKEN:
        logging.error("No TELEGRAM_BOT_TOKEN found in environment variables!")
        return

    # Build the application
    application = Application.builder().token(TOKEN).build()

    # Register the /start command handler
    application.add_handler(CommandHandler("start", start))

    # Start the bot using polling (ideal for Render Background Workers)
    logging.info("Bot is starting...")
    application.run_polling()

if __name__ == '__main__':
    main()
