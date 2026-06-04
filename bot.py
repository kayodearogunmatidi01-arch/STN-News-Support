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
        "សូមស្វាគមន៍មកកាន់ Nova News! 🚀\n\n"
        "ផ្លូវកាត់របស់អ្នកទៅកាន់ចំណងជើងសំខាន់ៗរបស់ពិភពលោក។ "
        "ទទួលបានព័ត៌មានថ្មីៗតាមពេលវេលាជាក់ស្តែង រៀបចំព្រឹត្តិការណ៍ជាសកល បច្ចេកវិទ្យា និងហិរញ្ញវត្ថុ ដោយគ្មានបញ្ហា។\n\n"
        "📌 ចុចលើ Start ដើម្បីប្ដូរព័ត៌មានរបស់អ្នកភ្លាមៗ"
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
