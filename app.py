from flask import Flask
import threading
import os
import logging

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Bot is running!"

# Import your bot client and run it in a thread
def start_bot():
    from main import bot
    bot.run()  # Pyrogram polling

if __name__ == "__main__":
    # Start bot in background thread
    thread = threading.Thread(target=start_bot)
    thread.daemon = True
    thread.start()
    
    # Run Flask server (foreground) on Render's PORT
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
