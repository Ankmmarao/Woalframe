import streamlit as st

from PIL import Image
logo = Image.open(r'C:\Users\India\Pictures\logo1.png')
# Wolfram Alpha API credentials
st.title("My Streamlit Bot")
st.set_page_config(page_title="Laptap  EDA", page_icon=":bar_chart:", layout="wide")
st.image(logo)
import telebot
import requests

# Define your Wolfram Alpha app ID
WOLFRAM_APP_ID = 'HY7933-YQ8VX4GA85'

# Telegram Bot API token
TELEGRAM_TOKEN='5935281977:AAG1RbxRDYBFg7Yvyx1jCtrnKOYhPQmFu04'

# Create an instance of the TeleBot class
bot = telebot.TeleBot(TELEGRAM_TOKEN)

# Handler for the /start command
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Hello! Send me a query and I'll search it on Wolfram Alpha.")

# Handler for incoming messages
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    query = message.text

    # Make a request to the Wolfram Alpha API
    url = f'http://api.wolframalpha.com/v1/result?appid={WOLFRAM_APP_ID}&i={query}'
    response = requests.get(url)
    result = response.text

    # Send the result back to the user
    bot.send_message(message.chat.id, result)

# Start the bot
bot.polling()
    # Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT
   
