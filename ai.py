import openai
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram.error import BadRequest

# OpenAI API Key
openai.api_key = "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"

# Telegram Bot Token
TELEGRAM_BOT_TOKEN = "7828379731:AAEMbd6RWe1iLV2SZRh3l6Cz6OC5Vm1BExQ"

# Admin ID
ADMIN_ID = 1786683163

# Function to generate funny responses using OpenAI
def generate_funny_response(user_input):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a funny and witty chatbot. Respond humorously to the user."},
                {"role": "user", "content": user_input}
            ]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return "Oops! Something went wrong. Try again later. 😅"

# Start command with inline keyboard
def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("Support Channel", url="https://t.me/creativeydv")],
        [InlineKeyboardButton("Support Group", url="https://t.me/v2ddos")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        "Hello! I'm your funny chatbot. Type anything, and I'll respond with humor! 😜\n\n"
        "Need help or support? Check out the options below:",
        reply_markup=reply_markup
    )

# Handle user messages
def handle_message(update: Update, context: CallbackContext):
    user_input = update.message.text
    response = generate_funny_response(user_input)
    update.message.reply_text(response)

# Broadcast message without pinning
def broadcast(update: Update, context: CallbackContext):
    if update.effective_user.id != ADMIN_ID:
        update.message.reply_text("You are not authorized to use this command.")
        return

    if len(context.args) == 0:
        update.message.reply_text("Please provide a message to broadcast.")
        return

    message = " ".join(context.args)
    for chat_id in context.bot_data.get("chats", []):
        try:
            context.bot.send_message(chat_id=chat_id, text=message, parse_mode=ParseMode.HTML)
        except Exception:
            continue

    update.message.reply_text("Broadcast sent successfully.")

# Broadcast message and pin it if bot is admin
def broadcastpin(update: Update, context: CallbackContext):
    if update.effective_user.id != ADMIN_ID:
        update.message.reply_text("You are not authorized to use this command.")
        return

    if len(context.args) == 0:
        update.message.reply_text("Please provide a message to broadcast and pin.")
        return

    message = " ".join(context.args)
    for chat_id in context.bot_data.get("chats", []):
        try:
            sent_message = context.bot.send_message(chat_id=chat_id, text=message, parse_mode=ParseMode.HTML)
            # Attempt to pin the message if bot is admin
            try:
                context.bot.pin_chat_message(chat_id=chat_id, message_id=sent_message.message_id)
            except BadRequest:
                pass  # Skip if bot is not admin
        except Exception:
            continue

    update.message.reply_text("Broadcast and pin sent successfully (if bot is admin).")

# Track chats for broadcasting
def track_chat(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    if "chats" not in context.bot_data:
        context.bot_data["chats"] = set()

    context.bot_data["chats"].add(chat_id)

# Main function
def main():
    # Create Updater and Dispatcher
    updater = Updater(token=TELEGRAM_BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    dispatcher.add_handler(CommandHandler("broadcast", broadcast))
    dispatcher.add_handler(CommandHandler("broadcastpin", broadcastpin))
    dispatcher.add_handler(MessageHandler(Filters.all, track_chat))

    # Start the bot
    updater.start_polling()
    print("Bot is running... Press Ctrl+C to stop.")
    updater.idle()

if __name__ == "__main__":
    main()
