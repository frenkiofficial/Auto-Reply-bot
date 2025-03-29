import logging
import json
import os
from telegram import Update, ForceReply
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# --- Configuration ---
# File names (change if you use different names)
TOKEN_FILE = 'token.txt'
CONFIG_FILE = 'config.json'

# --- Logging Setup ---
# Configure basic logging to see bot activity and errors
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO  # Set to logging.DEBUG for more detailed output
)
# Get a logger instance for this module
logger = logging.getLogger(__name__)

# --- Global Variable ---
# Dictionary to hold the keyword-reply pairs after loading
auto_replies = {}

# --- Core Functions ---

def load_config():
    """Loads keywords and replies from the JSON configuration file."""
    global auto_replies
    try:
        # Open and read the config file with UTF-8 encoding
        with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
            loaded_config = json.load(f)
        # Convert all keywords (keys) to lowercase for case-insensitive matching
        auto_replies = {key.lower(): value for key, value in loaded_config.items()}
        logger.info(f"Configuration successfully loaded from {CONFIG_FILE}")
    except FileNotFoundError:
        # Handle case where config file doesn't exist
        logger.warning(f"{CONFIG_FILE} not found. Creating an example file.")
        # Create a sample config if it's missing
        sample_config = {
            "hello": "Hi there!",
            "help": "Type /start for instructions."
        }
        try:
            with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
                # Write the sample config nicely formatted (indent=4)
                json.dump(sample_config, f, indent=4, ensure_ascii=False)
            # Load the newly created sample config
            auto_replies = {key.lower(): value for key, value in sample_config.items()}
        except Exception as e:
            logger.error(f"Could not create sample config file {CONFIG_FILE}: {e}")
            auto_replies = {} # Keep replies empty if creation fails
    except json.JSONDecodeError:
        # Handle case where JSON is invalid
        logger.error(f"Error decoding JSON from {CONFIG_FILE}. Please check its format.")
        auto_replies = {} # Use empty config if JSON is broken
    except Exception as e:
        # Catch any other unexpected errors during loading
        logger.error(f"An unexpected error occurred loading config: {e}")
        auto_replies = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends an explanation message when the /start command is issued."""
    user = update.effective_user # Get information about the user who sent /start
    # Construct the welcome message using HTML formatting
    message = (
        f"Hi {user.mention_html()}!\n\n"
        "I am the **Auto Reply Bot**.\n"
        "I will automatically reply to messages containing specific keywords.\n\n"
        f"⚙️ Keywords and replies are configured in the <code>{CONFIG_FILE}</code> file.\n"
        "✅ This bot works in both private chats and groups.\n\n"
        "Just send your message!"
    )
    # Send the message back to the user, parsing HTML tags
    await update.message.reply_html(message, disable_web_page_preview=True)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Checks incoming messages for keywords and sends replies."""
    # Ignore updates without a message or without text content
    if not update.message or not update.message.text:
        return

    # Get the message text and convert it to lowercase for case-insensitive matching
    message_text_lower = update.message.text.lower()
    chat_id = update.message.chat_id # Get chat ID for logging purposes
    message_id = update.message.message_id # Get message ID to reply directly

    # Iterate through the loaded keywords and their replies
    for keyword, reply in auto_replies.items():
        # Check if the (lowercase) keyword exists within the (lowercase) message text
        # This is a simple substring check.
        if keyword in message_text_lower:
            logger.info(f"Keyword '{keyword}' detected in chat {chat_id}. Replying...")
            try:
                # Send the corresponding reply back to the original message
                await update.message.reply_text(reply)
                # Stop checking for other keywords once the first match is found and replied to.
                # Remove 'break' if you want the bot to reply for *every* keyword match in a single message.
                break
            except Exception as e:
                # Log errors if sending the reply fails
                logger.error(f"Failed to send reply for keyword '{keyword}' in chat {chat_id}: {e}")

# --- Main Execution ---

def main() -> None:
    """Starts the bot."""
    # Load the keyword configuration when the bot starts
    load_config()

    # Read the bot token from the file
    try:
        with open(TOKEN_FILE, 'r') as f:
            TOKEN = f.read().strip() # Read token and remove leading/trailing whitespace
        if not TOKEN:
             raise ValueError("Token file exists but is empty.")
    except FileNotFoundError:
        logger.critical(f"Error: Token file '{TOKEN_FILE}' not found.")
        print(f"FATAL ERROR: The token file '{TOKEN_FILE}' was not found.")
        print("Please create this file and paste your Telegram Bot Token into it.")
        return # Stop execution if token file is missing
    except ValueError as e:
         logger.critical(f"Error reading token: {e}")
         print(f"FATAL ERROR: {e}")
         return # Stop execution if token is empty
    except Exception as e:
        logger.critical(f"An unexpected error occurred reading the token file: {e}")
        print(f"FATAL ERROR: Could not read token file: {e}")
        return # Stop for other file reading errors

    # Create the Application instance and pass in the bot's token.
    application = Application.builder().token(TOKEN).build()

    # --- Register Handlers ---
    # Register the /start command handler
    application.add_handler(CommandHandler("start", start))

    # Register a message handler for regular text messages (but not commands)
    # filters.TEXT: Matches any text message
    # ~filters.COMMAND: Excludes messages that start with '/' (commands)
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # --- Start the Bot ---
    logger.info("Starting bot polling...")
    print("Bot is running. Press Ctrl+C to stop.")
    # Start the bot and continuously fetch updates from Telegram
    application.run_polling()

# This ensures the main() function runs only when the script is executed directly
if __name__ == '__main__':
    main()