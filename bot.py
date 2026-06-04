import os
import sys
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Initialize standard platform logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", 
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Delivers the exact custom Khmer welcome dispatch when a user invokes /start."""
    welcome_text = (
        "Welcome!\n\n"
        "Thanks for joining. Use /start to begin and explore what I can do."
    )
    
    # Send response back to the user context
    if update.effective_message:
        await update.effective_message.reply_text(welcome_text)
        logger.info(f"Successfully processed /start for unique ID: {update.effective_user.id if update.effective_user else 'Unknown'}")

def main() -> None:
    # Safely fetch credentials from deployment parameters
    TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    
    if not TOKEN:
        logger.critical("🛑 FATAL: 'TELEGRAM_BOT_TOKEN' environment variable is missing on Render settings.")
        sys.exit(1)

    # Sanitize inputs to prevent trailing whitespaces
    TOKEN = TOKEN.strip()

    logger.info("Initializing asynchronous framework instance...")
    
    # Compile the polling application instance
    application = Application.builder().token(TOKEN).build()

    # Bind the structural start command string to our async callback
    application.add_handler(CommandHandler("start", start_command))

    # Engage the perpetual polling loop
    logger.info("🚀 Connection established! Application is actively polling for incoming traffic...")
    application.run_polling()

if __name__ == "__main__":
    main()
