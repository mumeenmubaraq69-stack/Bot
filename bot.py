import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# /start command function
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I am alive 🚀")

# Get the bot token from environment variables
TOKEN = os.getenv("BOT_TOKEN")

# Create the bot application
app = ApplicationBuilder().token(TOKEN).build()

# Add command handler
app.add_handler(CommandHandler("start", start))

# Run the bot
if __name__ == "__main__":
    app.run_polling()