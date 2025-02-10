from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

# Replace with your bot token
TOKEN = "1797648794:AAF_XxQavjEv6EBjcYXVSbshHqN8S9aXORQ"

# Correct channel ID
CHANNEL_CHAT_ID = "@kurd2025_1"

# Message IDs for each command
MESSAGE_IDS_COMMUNICATION = [2, 3]
MESSAGE_IDS_ANTENNA = [4, 5]

# Function to forward messages for /communication
async def forward_communication(update: Update, context: CallbackContext) -> None:
    try:
        for message_id in MESSAGE_IDS_COMMUNICATION:
            await context.bot.forward_message(chat_id=update.message.chat_id,
                                              from_chat_id=CHANNEL_CHAT_ID, 
                                              message_id=message_id)
        await update.message.reply_text(f"{len(MESSAGE_IDS_COMMUNICATION)} نامە نێردرا بۆ وانەی کۆمنیکەیشن.")
    except Exception as e:
        await update.message.reply_text(f"هەڵە ڕویدا: {str(e)}")

# Function to forward messages for /antenna
async def forward_antenna(update: Update, context: CallbackContext) -> None:
    try:
        for message_id in MESSAGE_IDS_ANTENNA:
            await context.bot.forward_message(chat_id=update.message.chat_id,
                                              from_chat_id=CHANNEL_CHAT_ID, 
                                              message_id=message_id)
        await update.message.reply_text(f"{len(MESSAGE_IDS_ANTENNA)} نامە نێردرا بۆ وانەی ئەنتێنا.")
    except Exception as e:
        await update.message.reply_text(f"هەڵە ڕویدا: {str(e)}")

# Start command handler
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("سڵاو\nبۆ وانەی کۆمنیکەیشن /communication دابگرە\nبۆ وانەی ئەنتێنا /antenna دابگرە")

def main():
    application = Application.builder().token(TOKEN).read_timeout(30).connect_timeout(30).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("communication", forward_communication))
    application.add_handler(CommandHandler("antenna", forward_antenna))

    application.run_polling()

if __name__ == "__main__":
    main()
