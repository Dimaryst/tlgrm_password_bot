import time
import telebot  # pip install pyTelegramBotApi
from telebot import types
import random
import string

import token_file
TOKEN = token_file.TOKEN

bot = telebot.TeleBot(TOKEN)

print(f"Bot started at {time.ctime()}")

def randomString(length):
    letters = string.ascii_letters + "0123456789"
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

# print info about incoming message
def terminal_output(message):
    print(f"User: \n{message.from_user}\n"
          f"Message: {message.text}\n\n")


@bot.message_handler(commands=['start'])
def intro(message):
    terminal_output(message)
    intro_message = "Hi! \n" \
                    "Look what I can do:  \n" \
                    "/new_password - generate the new random password with 16 symbols length\n"

    in_chat_markup = types.InlineKeyboardMarkup()
    link_btn = types.InlineKeyboardButton(text='MyGit', url='https://github.com/Dimaryst')
    in_chat_markup.add(link_btn)

    bot.send_message(message.chat.id, intro_message, reply_markup=in_chat_markup)


@bot.message_handler(commands=['new_password'])
def sendPassword(message):
    terminal_output(message)
    bot.send_message(message.chat.id, "Done! Your new password:")
    random_passphrase = randomString(16)
    bot.send_message(message.chat.id, random_passphrase)


bot.polling(none_stop=True)
