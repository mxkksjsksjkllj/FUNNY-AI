from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
import random

# Bot token and Admin ID
BOT_TOKEN = "7828379731:AAEMbd6RWe1iLV2SZRh3l6Cz6OC5Vm1BExQ"
ADMIN_ID = 1786683163

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("हैलो! 😊 मैं हूँ आपका मजेदार बॉट! बात करो, शायरी मांगो, या बस मस्ती करो! 😄")

# Broadcasting messages (Admin only)
async def broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id == ADMIN_ID:
        message = " ".join(context.args)
        if message:
            await update.message.reply_text("आपका संदेश ब्रॉडकास्ट हो रहा है...")
        else:
            await update.message.reply_text("कृपया कोई संदेश दें जिसे ब्रॉडकास्ट किया जा सके।")
    else:
        await update.message.reply_text("आपको इस कमांड का उपयोग करने की अनुमति नहीं है।")

# Funny chat response function with emoji and human-like behavior
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text.lower()

    # If user asks for a joke
    if "joke" in user_message or "जोकर" in user_message:
        jokes = [
            "क्यों हड्डी वाले एक-दूसरे से नहीं लड़ते? क्योंकि उनके पास हिम्मत नहीं होती! 😂",
            "मैंने अपने कंप्यूटर से कहा कि मुझे ब्रेक चाहिए, अब वो मुझे लगातार Kit-Kat भेज रहा है! 🍫😆",
            "क्यों रोबोट्स कभी घबराते नहीं? उनके पास स्टील की नसें होती हैं! 🤖💪"
        ]
        await update.message.reply_text(random.choice(jokes))
    
    # If user asks for a shayari
    elif "shayari" in user_message or "शायरी" in user_message:
        shayaris = [
            "चाँद की चाँदनी, सूरज की रौशनी, खुदा की नियत, हमारी मोहब्बत की सच्चाई! 🌙💖",
            "दिल की हर एक बात तुमसे कहने का मन करता है, मेरी शायरी भी तुमसे मिलने का मन करता है! 😘",
            "जिन्दगी के सफर में तुम हो साथ, तो हर दर्द भी लगता है आसान! 🌸💫"
        ]
        await update.message.reply_text(random.choice(shayaris))
    
    # If user is bored or feeling down
    elif "bored" in user_message or "बोर" in user_message:
        questions = [
            "अरे! बोर क्यों हो रहे हो? 😕 क्या कुछ नया ट्राई करना चाहोगे? 🎮🎨",
            "अगर बोर हो तो बताओ, कोई मजेदार खेल खेलते हैं! 🎉🙂",
            "कभी सोचा है कि तुम्हारी पसंदीदा चीज़ क्या है? 😃🍕"
        ]
        await update.message.reply_text(random.choice(questions))

    # General conversation with emojis
    else:
        responses = [
            "मैं बॉट हूं, लेकिन दिल से बात करता हूं! 😎",
            "क्या हाल है भाई? 😊 मुझे बताओ, कैसे हो? 🫣",
            "क्या तुमने आज कुछ नया सीखा? 🤔 या फिर बस मस्ती की? 😜"
        ]
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
  
