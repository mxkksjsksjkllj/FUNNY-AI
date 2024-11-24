from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.constants import ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Bot token and Admin ID
BOT_TOKEN = "7828379731:AAEMbd6RWe1iLV2SZRh3l6Cz6OC5Vm1BExQ"
ADMIN_ID = 1786683163

# Start command
def start(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    buttons = [
        [InlineKeyboardButton("Support Channel", url="https://t.me/creativeydv")],
        [InlineKeyboardButton("Support Group", url="https://t.me/v2ddos")]
    ]
    update.message.reply_text(
        "Welcome to the bot! Use the commands to interact.",
        reply_markup=InlineKeyboardMarkup(buttons),
        parse_mode=ParseMode.HTML
    )

# Broadcast command
def broadcast(update: Update, context: CallbackContext):
    if update.effective_user.id == ADMIN_ID:
        message = " ".join(context.args)
        if message:
            # Initialize bot_data if not already done
            if "chats" not in context.bot_data:
                context.bot_data["chats"] = []
            
            for chat_id in context.bot_data["chats"]:
                try:
                    context.bot.send_message(chat_id=chat_id, text=message)
                except:
                    continue
            update.message.reply_text("Broadcast sent successfully!")
        else:
            update.message.reply_text("Please provide a message to broadcast.")
    else:
        update.message.reply_text("You are not authorized to use this command.")

# Handle messages
def handle_message(update: Update, context: CallbackContext):
    user_message = update.message.text
    response = f"You said: {user_message}. Here's something funny: Why don't skeletons fight each other? They don't have the guts!"
    update.message.reply_text(response)

# Main function
def main():
    updater = Updater(BOT_TOKEN)
    dispatcher = updater.dispatcher

    # Handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("broadcast", broadcast))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
