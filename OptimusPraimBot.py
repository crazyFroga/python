import telebot
from telebot import types

bot = telebot.TeleBot('5742592434:AAGY9uclnYxzV-C7o6QIehe9T1OcFyWEoC4')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == 'Hello':
        bot.send_message(message.chat.id, "Hi!", parse_mode='html')
    elif message.text == 'My id':
        bot.send_message(message.chat.id, f"You ID:{message.from_user.id}", parse_mode='html')
    elif message.text == "Photo":
        Photo = open("Жёпа.jpg", "rb")
        bot.send_photo(message.chat.id, Photo )
    else:
        bot.send_message(message.chat.id, "Fack you!", parse_mode='html')




@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Посетить веб сайт", url="https://pypi.org/project/pyTelegramBotAPI/"))
    bot.send_message(message.chat.id, "Быром тыкни,утка!", reply_markup=markup)



@bot.message_handler(commands=['help'])
def website(message):
    markup = types.ReplyKeyboardMarkup()
    website = types.KeyboardButton("Сайт")
    start = types.KeyboardButton("Start")
    markup.add(website, start)
    bot.send_message(message.chat.id, "Быром тыкни,я то укушу!", reply_markup=markup)


bot.polling(none_stop=True)
