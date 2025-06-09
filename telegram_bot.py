import os
import httpx
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv
from crypto_agent import create_agent

# Load environment variables
load_dotenv()

# Initialize crypto agent
crypto_agent = create_agent()

def get_proxy_config():
    """Get proxy configuration from environment variables."""
    proxy_url = os.getenv("PROXY_URL")
    proxy_username = os.getenv("PROXY_USERNAME")
    proxy_password = os.getenv("PROXY_PASSWORD")
    
    if not proxy_url:
        return None
    
    # Build proxy URL with authentication if provided
    if proxy_username and proxy_password:
        # Parse the proxy URL to insert credentials
        if "://" in proxy_url:
            protocol, rest = proxy_url.split("://", 1)
            proxy_url = f"{protocol}://{proxy_username}:{proxy_password}@{rest}"
    
    return proxy_url

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        f"Hi {user.mention_html()} 👋\n"
        "Tôi có thể giúp bạn phân tích thị trường crypto.\n"
        f"Ví dụ: @{context.bot.username} phân tích BTC/USDT"
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle messages that mention the bot."""
    message = update.message.text
    bot_username = context.bot.username

    # Check if message mentions the bot
    if f"@{bot_username}" in message:
        # Remove bot mention from message
        query = message.replace(f"@{bot_username}", "").strip()
        
        # Send processing message
        processing_msg = await update.message.reply_text(
            "⏳ Đang phân tích..."
        )
        
        try:
            # Get response from crypto agent
            response = crypto_agent.run(query)
            # Update the processing message with results
            await processing_msg.edit_text(response)
        except Exception as e:
            # Update the processing message with error
            await processing_msg.edit_text(
                "❌ Có lỗi xảy ra. Vui lòng thử lại sau."
            )

def main() -> None:
    """Start the bot."""
    # Get proxy configuration
    proxy_url = get_proxy_config()
    
    # Create the Application with proxy support
    builder = Application.builder().token(os.getenv("TELEGRAM_BOT_TOKEN"))
    
    if proxy_url:
        # Configure with proxy - pass the URL string directly
        builder = builder.proxy(proxy_url).get_updates_proxy(proxy_url)
        print(f"🌐 Sử dụng proxy: {proxy_url.split('@')[-1] if '@' in proxy_url else proxy_url}")
    else:
        print("🔗 Kết nối trực tiếp (không sử dụng proxy)")
    
    application = builder.build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 Bot đang khởi động...")
    
    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main() 