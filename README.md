# ✨ Auto Reply Telegram Bot ✨

A simple, easy-to-configure Telegram bot that automatically replies to messages based on predefined keywords. Works seamlessly in both private chats and groups.

This bot provides a basic foundation for automated responses on Telegram.

---

## ✅ Core Features (Included)

*   **Keyword-Based Replies:** Automatically responds when a message contains specific keywords.
*   **Group & Private Chat Compatible:** Functions correctly whether you add it to a group or chat with it directly.
*   **Easy JSON Configuration:** Keywords and their corresponding replies are managed in a simple `config.json` file.
*   **/start Command:** Provides users with initial instructions on how the bot works.
*   **Case-Insensitive Matching:** Detects keywords regardless of capitalization (e.g., "Hello", "hello", "HELLO" are treated the same).

---

## 🚀 Getting Started: Setup & Usage Guide

Follow these steps to get your Auto Reply Bot up and running:

1.  **Clone or Download:**
    *   Get the code: Clone this repository or download the source code ZIP from the repository page.
    ```bash
    git clone https://github.com/frenkiofficial/Auto-Reply-bot.git
    cd Auto-Reply-bot          # Navigate into the project directory
    ```
    *   If you downloaded a ZIP, extract it and navigate into the folder using your terminal or command prompt.

2.  **(Recommended) Create a Virtual Environment:**
    *   This keeps project dependencies isolated.
    ```bash
    python -m venv venv
    # Activate on Windows
    .\venv\Scripts\activate
    # Activate on macOS/Linux
    source venv/bin/activate
    ```

3.  **Install Dependencies:**
    *   Install the required Python library (`python-telegram-bot`).
    ```bash
    pip install -r requirements.txt
    ```

4.  **Get Your Telegram Bot Token:**
    *   Open Telegram and search for `@BotFather`.
    *   Send `/newbot` and follow the instructions to create your bot.
    *   BotFather will give you an **API Token**. **Keep this token secure and private!**

5.  **Store Your Token:**
    *   Create a file named `token.txt` in the main project directory (`Auto-Reply-bot/`).
    *   Paste **only** your API Token into this file and save it.

6.  **Configure Keywords & Replies:**
    *   Open the `config.json` file.
    *   Edit the keywords (keys) and their replies (values).
        *   **Keywords (keys):** Should be in lowercase. The bot will match these case-insensitively within user messages.
        *   **Replies (values):** The text the bot should send back.
    *   Example `config.json`:
        ```json
        {
          "hello": "Hi there! Welcome.",
          "support": "For support, please email support@example.com.",
          "price list": "You can find our prices here: [Your Link]"
        }
        ```
    *   Save the `config.json` file (ensure it's saved with UTF-8 encoding).

7.  **Run the Bot:**
    *   Execute the main Python script from your terminal (make sure you are inside the `Auto-Reply-bot` directory):
    ```bash
    python main.py
    ```
    *   You should see output like "Starting bot polling..." and "Bot is running...".
    *   Your bot is now active!

8.  **Test Your Bot:**
    *   Find your bot on Telegram (using the username you gave it).
    *   Send `/start`.
    *   Send messages containing the keywords you added to `config.json`.
    *   Add the bot to a group and test it there too.

**Note:** If you modify `config.json` while the bot is running, you'll need to stop the bot (Ctrl+C in the terminal) and restart it (`python main.py`) for the changes to take effect.

---

## 🛠️ Need More Features? Custom Development Available! 🔥

This bot provides essential auto-reply functionality. However, if you require more advanced capabilities or custom integrations, I can help build them for you!

Here are some examples of features I can add:

*   **🔹 Image/Sticker Replies:** Configure the bot to respond with specific images or stickers based on keywords.
*   **🧠 AI-Powered Replies (OpenAI/Gemini):** Integrate powerful AI models like ChatGPT or Gemini for more intelligent, context-aware, and conversational responses.
*   **🔄 Randomized Replies:** Define multiple reply options for a single keyword, and the bot will choose one randomly.
*   **🚫 Anti-Spam Mode:** Implement rate limiting or cooldowns to prevent users from spamming keywords excessively.
*   **📊 Google Sheets Logging:** Automatically log incoming messages and the bot's replies to a Google Sheet for tracking and analysis.
*   **⚙️ In-Chat Configuration:** Add commands to allow authorized users to add/edit/remove keywords and replies directly via Telegram chat.
*   ...and much more tailored to your specific needs!

---

## 📞 Get in Touch for Custom Features!

Interested in enhancing this bot or developing a custom Telegram solution? Reach out to me!

*   **⭐ Fiverr:** [frenkimusic on Fiverr](https://www.fiverr.com/frenkimusic/)
*   **✈️ Telegram:** [@FrenkiOfficial](https://t.me/FrenkiOfficial)
*   **🐙 GitHub:** [frenkiofficial](https://github.com/frenkiofficial)
*   **🤗 Hugging Face:** [frenkiofficial](https://huggingface.co/frenkiofficial)
*   **🐦 Twitter / X:** [@officialfrenki](https://twitter.com/officialfrenki)

Let's discuss how we can build the perfect bot for you!

---

## 📜 License

This basic bot code is typically provided under a permissive license like MIT (you can add the specific license file if you wish). Custom development work will be discussed on a case-by-case basis.
