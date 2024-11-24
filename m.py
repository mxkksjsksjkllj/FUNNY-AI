from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

# Bot token and Admin ID
BOT_TOKEN = "7828379731:AAEMbd6RWe1iLV2SZRh3l6Cz6OC5Vm1BExQ"
ADMIN_ID = 1786683163

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome to the bot! Type anything to interact.")

# Broadcast command (Admin only)
async def broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id == ADMIN_ID:
        message = " ".join(context.args)
        if message:
            await update.message.reply_text("Broadcasting your message...")
        else:
            await update.message.reply_text("Please provide a message to broadcast.")
    else:
        await update.message.reply_text("You are not authorized to use this command.")

# Handle user messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    await update.message.reply_text(f"You said: {user_message}")

# Main function to start the bot
def main():
    app = Application.builder().token(BOT_TOKEN).build()

    # Add command and message handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("broadcast", broadcast))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Run the bot
    app.run_polling()

if __name__ == "__main__":
    main()
