from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
import random

# Bot token and Admin ID
BOT_TOKEN = "7828379731:AAEMbd6RWe1iLV2SZRh3l6Cz6OC5Vm1BExQ"
ADMIN_ID = 1786683163

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome to the funny bot! Type anything, and let's have some fun!")

# Broadcasting messages (Admin only)
async def broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id == ADMIN_ID:
        message = " ".join(context.args)
        if message:
            await update.message.reply_text("Broadcasting your message...")
        else:
            await update.message.reply_text("Please provide a message to broadcast.")
    else:
        await update.message.reply_text("You are not authorized to use this command.")

# Funny chat response function
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text.lower()

    # List of funny responses in Hindi
    responses = [
        "Main ek bot hoon, mere paas bhawnaayein nahi hain, lekin main hamari baaton ka mazaa le raha hoon!",
        "Kya aap jaante hain? Main hasi nahi hasa sakta, lekin main abhi bhi mazedaar hoon!",
        "Kyun bots kabhi raaz nahi batate? Kyunki hum hamesha bits spill kar dete hain!",
        "Main ek bot hoon, lekin main achha samay bitana jaanta hoon!",
        "Agar mere paas har baar 'hi' kehne par ek paisa hota, to main abhi bhi bot hota, lekin ek ameer bot!"
    ]
    
    # If user asks for a joke in English or Hindi
    if "joke" in user_message:
        jokes = [
            "Why don't skeletons fight each other? They don't have the guts!",
            "I told my computer I needed a break, now it won’t stop sending me Kit-Kats.",
            "Why don’t robots ever panic? They have nerves of steel!"
        ]
        await update.message.reply_text(random.choice(jokes))
    # If the message contains the word "how" or "what"
    elif "how" in user_message or "what" in user_message:
        await update.message.reply_text("Main ek bot hoon, mere paas sabhi jawab nahi hote, lekin main aapko jokes zaroor bata sakta hoon!")
    # Default funny responses
    else:
        await update.message.reply_text(random.choice(responses))

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
  
