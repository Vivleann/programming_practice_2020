import sys
import random

import telebot

bot = telebot.TeleBot('1435222126:AAFVkh_lxh7B48Y13aX8riY1HaZTA9qWoB0')


@bot.message_handler(commands=['choose_group'])
def start_message(message):
    keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
    keyboard1.row('Физико-математические')
    keyboard1.row('Естественные', 'Гуманитарные')
    bot.send_message(message.chat.id, 'Привет, выбери профиль олимпиады', reply_markup=keyboard1)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')
    
@bot.message_handler(content_types=['text'])
def send_text(message):
   
    if message.text.lower() == 'физико-математические':
        
        keyboard2 = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard2.row('Физика', 'Матан')
        bot.send_message(message.chat.id, 'Выбери предмет', reply_markup=keyboard2)

    elif message.text.lower() == 'естественные':
        keyboard3 = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard3.row('Химия', 'Биология', 'География')
        bot.send_message(message.chat.id, 'Выбери предмет', reply_markup=keyboard3)
    elif message.text.lower() == 'гуманитарные':
        keyboard4 = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard4.row('Литература', 'Русский')
        keyboard4.row('Английский', 'История', 'Обществознание')
        bot.send_message(message.chat.id, 'Выбери предмет', reply_markup=keyboard4)
    elif message.text.lower() == 'физика':
        text = '[Физтех](https://olymp.mipt.ru/)'
        bot.send_message(message.chat.id, text + " /phystech", parse_mode='MarkdownV2')
        bot.send_message(message.chat.id, 'Физтех (1 уровень) /phystech')
        bot.send_message(message.chat.id, 'Покори Воробьевы горы (1 уровень) /gori')


@bot.message_handler(content_types=['number'])
def handle_text(message):
    print(message)
    
    pred = random.randint(1, 100)
    mess = 'Вот тебе случайное число!'    
    bot.send_message(message.chat.id, pred)

bot.polling()